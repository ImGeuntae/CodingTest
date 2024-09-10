def solution(nums):
    answer = 0
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                x = sum([nums[i],nums[j],nums[k]])
                for a in range(2,int(x**0.5)+1):
                    if x%a == 0:
                        break
                else:
                    answer += 1
    return answer