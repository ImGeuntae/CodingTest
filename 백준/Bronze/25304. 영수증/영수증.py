N = int(input())
for _ in range(int(input())):
    A,B = map(int, input().split())
    N -= A*B
if N==0:
    print("Yes")
else:
    print("No")
