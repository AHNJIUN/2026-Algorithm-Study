def solution(nums):
    lst = set(nums)
    return len(lst) if len(lst)<=len(nums)//2 else len(nums)//2