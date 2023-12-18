import sys
input()
S = set(sys.stdin.readline().split())
input()
for i in sys.stdin.readline().split():
    print(1 if i in S else 0)