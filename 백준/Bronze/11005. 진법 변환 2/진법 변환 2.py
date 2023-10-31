base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N,B = map(int,input().split())
answer = ""
while N:
    answer += base[N%B]
    N //= B    
print(answer[::-1])