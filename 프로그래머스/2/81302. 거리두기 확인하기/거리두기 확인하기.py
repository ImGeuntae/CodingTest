def solution(places):
    ans = [1]*5
    for i in range(5):
        P = []
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    P += [(j,k)]
        for x,y in P:
            for q,r in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=q<5 and 0<=r<5 and places[i][q][r] == "P":
                    ans[i] = 0
                    break
            else:
                for q,r in [(x+2,y),(x-2,y),(x,y+2),(x,y-2)]:
                    if 0<=q<5 and 0<=r<5 and places[i][q][r] == "P" and places[i][(q+x)//2][(r+y)//2] == "O":
                        ans[i] = 0
                        break
                else:
                    for q,r in [(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1)]:
                        if 0<=q<5 and 0<=r<5 and places[i][q][r] == "P" and (places[i][q][y] == "O" or places[i][x][r] == "O"):
                            ans[i] = 0
                            break
    return ans