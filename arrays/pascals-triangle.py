def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    answer = []
    for i in range(numRows):
        answer.append([])
        answer[i].append(1)
        for j in range(1, i):
            answer[i].append(answer[i-1][j-1] + answer[i-1][j])
        if i > 0:
            answer[i].append(1)
    return answer
        