from math import factorial
x,y = map(int,input().split())
a,b = map(int,input().split())
print((factorial(a+b-2)//(factorial(a-1)*factorial(b-1)))*(factorial(x+y-a-b)//(factorial(x-a)*factorial(y-b)))%1000007)