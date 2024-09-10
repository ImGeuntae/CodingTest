def solution(mats, park):
    answer = -1
    Y,X = len(park),len(park[0])
    for y in range(Y):
        for x in range(X):
            if park[y][x] == '-1':
                n = 1
                while True:
                    c = [[i,j] for i in range(n) for j in range(n) if i==n-1 or j==n-1]
                    for a,b in c:
                        a,b = y+a, x+b
                        if a>=Y or b>=X or park[a][b] != '-1':
                            break
                    else:
                        if n in mats and n > answer:
                            answer = n
                        n += 1
                        continue
                    break
    return answer
                    
                    
                            
                    