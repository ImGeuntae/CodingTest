S = input().upper()
dic = dict.fromkeys(S)
for k,v in dic.items():
    dic[k] = S.count(k)
Z = sorted(dic, key=lambda x:dic[x], reverse=True)[:min(len(dic),2)]
if len(Z)==1 or (dic[Z[0]] != dic[Z[1]]):
    print(Z[0])
else:
    print("?")