def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1,distance
    while left <= right:
        N,now,middle = n,0,(left+right)//2
        R = []
        for r in rocks:
            if r-now < middle:
                N -= 1
                if N < 0:
                    right = middle - 1
                    break
            else:
                now = r
                R.append(r)
        else:
            now  = distance
            for r in R[::-1]:
                if now-r < middle:
                    N -= 1
                else:
                    break
            if N < 0:
                right = middle - 1
            else:
                left = middle + 1
                ans = middle 
    return ans