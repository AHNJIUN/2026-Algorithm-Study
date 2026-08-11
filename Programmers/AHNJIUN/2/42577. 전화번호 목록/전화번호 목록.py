def solution(phone_book):
    x = set(phone_book) # phone_book 원소들을 해시로 변환(집합화)
    for num in x:
        s = ""
        for c in num[:-1]:  
            s+=c
            if s in x:
                return False          
    return True