def solution(numbers):
    n = list(numbers)
    cnt = 0
    lst = set()
    def permutation(remain, path):
        if path: 
            lst.add(int("".join(path)))
        for i in range(len(remain)):
            permutation(remain[:i]+remain[i+1:],path + [remain[i]])
    def is_prime(x):
        if x < 2:
            return False
        for j in range(2,x):
            if x%j==0:
                return False
        return True
    permutation(n,[])
    return len([x for x in lst if is_prime(x)])