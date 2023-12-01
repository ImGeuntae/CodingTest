L = [1]*10
for _ in range(int(input())-1):
    L = [sum(L[:i+1]) for i in range(10)]
print(sum(L)%10007)