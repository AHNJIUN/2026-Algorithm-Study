# 첫 번쨰 방법
from functools import cmp_to_key

def compare(a,b):
    if a+b > b+a:
        return -1
    else:
        return 1
    
def solution(numbers):
    answer = ''
    nums = list(map(str, numbers))

    nums.sort(key=cmp_to_key(compare))
    answer = "".join(nums)
    if answer[0]=="0":
        return "0"
    return answer

# 두 번째 방법
