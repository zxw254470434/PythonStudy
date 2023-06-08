def lengthOfLastWord(s: str):
    return len(s.strip(" ").split(" ")[-1])


s = "luffy is still joyboy"
print(lengthOfLastWord(s))
