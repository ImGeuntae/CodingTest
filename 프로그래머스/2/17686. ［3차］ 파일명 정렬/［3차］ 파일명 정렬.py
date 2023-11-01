def solution(files):
    dic = dict()
    for i in files:
        h = n = ""
        for j in i:
            if not j.isdigit():
                if n:
                    break
                h += j
            else:
                n += j
        dic[i] = (h.lower(),str(int(n)))
    return sorted(dic,key=lambda x:(dic[x][0],int(dic[x][1])))