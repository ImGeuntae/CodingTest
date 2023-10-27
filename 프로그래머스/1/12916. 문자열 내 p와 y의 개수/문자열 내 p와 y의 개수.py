def solution(s):
    PY = [1 if (x=="p" or x=="P") else -1 if (x=="y" or x=="Y") else 0 for x in s]
    return False if sum(PY) else True