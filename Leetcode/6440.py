def differenceOfDistinctValues(grid):
    m = len(grid)
    n = len(grid[0])
    answer = []

    for i in range(0, m):
        answer_row = []
        for j in range(0, n):
            topLeft = set()
            bottomRight = set()

            index_row = i
            index_clo = j
            while index_row > 0 and index_clo > 0:
                index_row -= 1
                index_clo -= 1
                topLeft.add(grid[index_row][index_clo])

            index_row = i
            index_clo = j
            while index_row < m-1 and index_clo < n-1:
                index_row += 1
                index_clo += 1
                bottomRight.add(grid[index_row][index_clo])

            answer_row.append(abs(len(topLeft) - len(bottomRight)))
        answer.append(answer_row)

    return answer


grid = [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
print(differenceOfDistinctValues(grid))


grid2 = [[1]]
print(differenceOfDistinctValues(grid2))