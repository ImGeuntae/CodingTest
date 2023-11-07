def solution(sticker):
    h = len(sticker)
    if h < 3:
        return max(sticker)
    else:
        M, m = [0]*h, [0]*(h-1)
        M[0], M[1], m[0], m[1] = 0, sticker[1], sticker[0], sticker[0]
        for i in range(2,h):
            M[i] = max(M[i-1], M[i-2] + sticker[i])
        for i in range(2, h-1):
            m[i] = max(m[i-1], m[i-2] + sticker[i])
        return max(M[-1],m[-1])