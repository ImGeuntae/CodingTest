n,a,b = int(input()),1,0
print((n!=0)*(2*(n>0 or n%2)-1))
for _ in range(abs(n)):
    a,b = b,(a+b)%1000000000
print(b)