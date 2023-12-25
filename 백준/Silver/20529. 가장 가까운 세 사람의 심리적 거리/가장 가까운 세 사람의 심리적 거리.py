for _ in range(int(input())):
    if (n:=int(input()))>32:
        input()
        print(0)
    else:
        MBTI = input().split()
        ans = 12
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    ans = min(ans,sum((x!=y)+(y!=z)+(z!=x) for x,y,z in zip(MBTI[i],MBTI[j],MBTI[k])))
        print(ans)