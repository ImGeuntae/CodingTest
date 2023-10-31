alpha_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
D = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
S = 0
for i in input():
    S += D[alpha_list.index(i)] + 1
print(S)