def solution(numbers, hand):
    H = {"L": 10, "R": 12}
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
            L, R = abs(H["L"]-n), abs(H["R"]-n)
            L, R = L//3 + L%3, R//3 + R%3
            if L < R or (L == R and hand[0] == "l"):
                ans += "L"
                H["L"] = n
            else:
                ans += "R"
                H["R"] = n
    return ans