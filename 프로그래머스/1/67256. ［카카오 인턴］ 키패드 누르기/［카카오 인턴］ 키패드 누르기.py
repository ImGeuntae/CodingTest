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
            L = abs(H["L"]-n)
            L = L//3 + L%3
            R = abs(H["R"]-n)
            R = R//3 + R%3
            if L < R:
                ans += "L"
                H["L"] = n
            elif L > R:
                ans += "R"
                H["R"] = n
            else:
                h = hand[0].upper()
                ans += h
                H[h] = n
    return ans