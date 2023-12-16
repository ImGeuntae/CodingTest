import sys
L=set(input() for _ in range(int(input())))
print(*sorted(L,key=lambda x:[len(x),x]))