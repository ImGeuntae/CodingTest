from math import factorial as f
n = f(int(input()))
ans = 0
while not n%10:
    n //= 10
    ans += 1
print(ans)