def solution(park, routes):
    a,b = len(park), len(park[0])
    block = []
    for x in range(a):
        for y in range(b):
            if park[x][y] == "S":
                S = [x,y]
            elif park[x][y] == "X":
                block.append([x,y])
    D = {"E": [0,1], "W": [0,-1], "S": [1,0], "N": [-1,0]}
    for r in routes:
        d,n = r.split()
        d, SS = D[d], S
        for _ in range(int(n)):
            if (0<= SS[0]+d[0] < a) and (0<= SS[1]+d[1] < b):
                SS = [SS[0]+d[0],SS[1]+d[1]]
                if SS in block:
                    break
            else:
                break
        else:
            S = SS
    return S