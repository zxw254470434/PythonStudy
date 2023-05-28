import os
import sys
import logging
import datasets
import evaluate

import pandas as pd
import numpy as np

from transformers import AutoModelForSequenceClassification, DebertaV2Tokenizer, DataCollatorWithPadding
from transformers import Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_int8_training, TaskType
from sklearn.model_selection import train_test_split

train = pd.read_csv("./corpus/train.csv", header=0, delimiter="\t", quoting=3)
val = pd.read_csv("./corpus/dev.csv", header=0, delimiter='\t', quoting=3)
test = pd.read_csv("./corpus/test.csv", header=0, delimiter="\t", quoting=3)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info(r"running %s" % ''.join(sys.argv))

    # 处理、加载数据集
    # train, val = train_test_split(train, test_size=.2)

    train_dict = {'label': train["lable"], 'text': train['text_a']}
    val_dict = {'label': val["lable"], 'text': val['text_a']}
    test_dict = {"text": test['text_a']}

    train_dataset = datasets.Dataset.from_dict(train_dict)
    val_dataset = datasets.Dataset.from_dict(val_dict)
    test_dataset = datasets.Dataset.from_dict(test_dict)

    batch_size = 32

    # 加载分词器
    model_id = "microsoft/deberta-v2-xxlarge"
    tokenizer = DebertaV2Tokenizer.from_pretrained(model_id)


    # 创建预处理函数，标记和截断序列
    def preprocess_function(examples):
        return tokenizer(examples['text'], truncation=True)


    # 将预处理函数映射到整个数据集
    tokenized_train = train_dataset.map(preprocess_function, batched=True)
    tokenized_val = val_dataset.map(preprocess_function, batched=True)
    tokenized_test = test_dataset.map(preprocess_function, batched=True)

    # 动态填充
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    # 创建标签到id的映射
    id2lable = {0: '科技', 1: '体育', 2: '时政', 3: '股票', 4: '娱乐', 5: '教育', 6: '家居', 7: '财经', 8: '房产',
                9: '社会', 10: '游戏', 11: '彩票', 12: '星座', 13: '时尚'}
    lable2id = {'科技': 0, '体育': 1, '时政': 2, '股票': 3, '娱乐': 4, '教育': 5, '家居': 6, '财经': 7, '房产': 8,
                '社会': 9, '游戏': 10, '彩票': 11, '星座': 12, '时尚': 13}

    # 加载预训练模型
    model = AutoModelForSequenceClassification.from_pretrained(model_id, num_lables=14, id2lable=id2lable,
                                                               lable2id=lable2id)

    # Define LoRA Config
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        # target_modules=['q_proj', 'v_proj'],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.SEQ_CLS
    )

    # prepare int-8 model for training
    # model = prepare_model_for_int8_training(model)

    # add LoRA adaptor
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # 创建评价函数
    metric = evaluate.load("accuracy")


    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)


    training_args = TrainingArguments(
        output_dir='./checkpoint',  # output directory
        num_train_epochs=3,  # total number of training epochs
        per_device_train_batch_size=2,  # batch size per device during training
        per_device_eval_batch_size=4,  # batch size for evaluation
        warmup_steps=500,  # number of warmup steps for learning rate scheduler
        weight_decay=0.01,  # strength of weight decay
        logging_dir='./logs',  # directory for storing logs
        logging_steps=100,
        save_strategy="no",
        evaluation_strategy="epoch"
    )

    trainer = Trainer(
        model=model,  # the instantiated 🤗 Transformers model to be trained
        args=training_args,  # training arguments, defined above
        train_dataset=tokenized_train,  # training dataset
        eval_dataset=tokenized_val,  # evaluation dataset
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    trainer.train()

    prediction_outputs = trainer.predict(tokenized_test)
    test_pred = np.argmax(prediction_outputs[0], axis=-1).flatten()
    print(test_pred)

    result_output = pd.DataFrame(data={"id": test["id"], "sentiment": test_pred})
    result_output.to_csv("./result/deberta_lora_int8.csv", index=False, quoting=3)
    logging.info('result saved!')
