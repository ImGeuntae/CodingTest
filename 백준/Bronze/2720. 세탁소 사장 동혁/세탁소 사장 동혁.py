for _ in range(int(input())):
    N = int(input())
    print(N//25, (N%25)//10, ((N%25)%10)//5, ((N%25)%10)%5)