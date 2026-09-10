def solution(array, commands):
    answer = []
    for start, end, k in commands:
        lst = sorted(array[start-1:end])
        answer.append(lst[k-1])
    return answer