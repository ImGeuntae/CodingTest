def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = 1
    for j in phone_book:
        for k in range(len(j)-1):
            if j[:k+1] in dic:
                return False
    return True