n = input().split("-")
a = sum(map(int,n[0].split('+')))
b = sum(sum(map(int,x.split('+'))) for x in n[1:])
print(a-b)