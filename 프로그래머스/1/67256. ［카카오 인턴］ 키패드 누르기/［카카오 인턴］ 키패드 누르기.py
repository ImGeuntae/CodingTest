def solution(numbers, hand):
    H = {"L": 10, "R": 12}
    D = {1,2,3,4,5,6,7,8,9,0,'*','#'}
    ans = ""
    for n in numbers:
        if n in [1,4,7]:
            H["L"] = n
            ans += "L"
        elif n in [3,6,9]:
            H["R"] = n
            ans += "R"
        else:
            if n == 0:
                n = 11
            L, R = sum(divmod(abs(H["L"]-n),3)), sum(divmod(abs(H["R"]-n),3))
            if L < R or (L == R and hand[0] == "l"):
                ans += "L"
                H["L"] = n
            else:
                ans += "R"
                H["R"] = n
    return ans