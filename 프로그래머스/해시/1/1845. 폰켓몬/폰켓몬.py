def solution(nums):
    n = len(nums)
    x = n/2
    y = len(set(nums))
    if y <= x:
        answer = y
    else:
        answer = x
    return answer