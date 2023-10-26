def solution(phone_book):
    hash_map = dict.fromkeys(phone_book)
    for j in phone_book:
        for k in range(len(j)-1):
            if j[:k+1] in hash_map:
                return False
    return True