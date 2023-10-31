S = input().upper()
dic = dict.fromkeys(S)
for k,v in dic.items():
    dic[k] = S.count(k)
s = [k for k,v in dic.items() if max(dic.values()) == v]
if len(s) >= 2:
    print("?")
else:
    print(s[0])