def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1,distance
    while left <= right:
        N,now,mid = n,0,(left+right)//2
        for r in rocks:
            if r-now < mid:
                N -= 1
                if N < 0:
                    right = mid - 1
                    break
            else:
                now = r
        else:
            left = mid + 1
            ans = mid
    return ans