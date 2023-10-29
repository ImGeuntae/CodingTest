def solution(s):
    s = sorted(s.split(" "), key=lambda x:int(x))
    return "{} {}".format(s[0], s[-1])