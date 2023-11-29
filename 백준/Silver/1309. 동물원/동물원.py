a,b = 1,1
for _ in range(int(input())):
    a,b = a+b+b,a+b
print(a%9901)