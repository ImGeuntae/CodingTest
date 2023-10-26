def solution(s, skip, index):
    alphabet = [i for i in list("abcdefghijklmnopqrstuvwxyz") if i not in skip]
    answer = ""
    for j in s:
        answer += alphabet[((alphabet.index(j)) + index)%len(alphabet)]
    return answer