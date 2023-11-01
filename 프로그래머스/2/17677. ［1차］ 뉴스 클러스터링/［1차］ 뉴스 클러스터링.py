def solution(str1, str2):
    str1 = [(str1[i]+str1[i+1]).lower() for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha()]
    str2 = [(str2[i]+str2[i+1]).lower() for i in range(len(str2)-1) if (str2[i]+str2[i+1]).isalpha()]
    A = sum([min(str1.count(j),str2.count(j)) for j in (set(str1) & set(str2))])
    O = sum([max(str1.count(j),str2.count(j)) for j in (set(str1) | set(str2))])
    return int((A/O)*65536) if O else 65536