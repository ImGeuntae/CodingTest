alpha_list = "abcdefghijklmnopqrstuvwxyz"
ans = ["-1"]*26
for idx, i in enumerate(input()):
    if ans[alpha_list.index(i)] == "-1":
        ans[alpha_list.index(i)] = str(idx)
print(' '.join(ans))