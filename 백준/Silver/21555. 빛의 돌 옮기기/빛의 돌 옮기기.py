from collections import deque
import sys
N,K = map(int,input().split())
a=b=0
A=deque(map(int,sys.stdin.readline().split()))
B=deque(map(int,sys.stdin.readline().split()))
for _ in range(N):
    x,y=A.popleft(),B.popleft()
    a,b=min(a,b+K)+x,min(b,a+K)+y
print(min(a,b))