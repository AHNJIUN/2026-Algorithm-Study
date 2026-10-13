def solution(numbers):
    numbers = list(map(str,numbers))
    lst = sorted([(n*3,i) for i,n in enumerate(numbers)],reverse=True)
    return ''.join([numbers[b] for a,b in lst]) if lst[0][0][0]!="0" else "0"