def solution(msg):
    dic = {alp: idx for idx, alp in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",start=1)}
    idx = 27
    answer = []
    while msg:
        i=1
        while (len(msg)>=i) and (msg[:i] in dic):
            i += 1
        answer.append(dic[msg[:i-1]])
        dic[msg[:i]] = idx
        msg = msg.replace(msg[:i-1],'',1)
        idx += 1
    return answer