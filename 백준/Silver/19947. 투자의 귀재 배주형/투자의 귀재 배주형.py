H,Y = map(int,input().split())
dp = [H]
for y in range(Y):
    if y>3:
        dp.append(int(max(dp[-1]*1.05,dp[-3]*1.2,dp[-5]*1.35)))
    elif y>1:
        dp.append(int(max(dp[-1]*1.05,dp[-3]*1.2)))
    else:
        dp.append(int(dp[-1]*1.05))
print(dp[-1])