def solution(s):
    d = []
    for c in s:
        if c=="(": 
            d.append("(")
        elif not d: 
            return False
        else: d.pop()
    return len(d)==0