"""
Short function that transposes a matrix
Returns a matrix with the columns and rows of the input matrix reversed
As an example: 
            [[1, 1, 2],
            [3, 5, 8],
            [13, 21, 34]]
Would get an output of:
            [[1, 3, 13],
            [1, 5, 21],
            [2, 8, 34]]
No practical applications included but could come in handy for data manipulation
"""
def transposeMatrix(data):
    i = 0
    answer = []
    while True:
        col = []
        for row in data:
            col.append(row[i])
        answer.append(col)
        i = i + 1
        if len(data[0]) <= i:
            break
    #replace this for solution
    return answer