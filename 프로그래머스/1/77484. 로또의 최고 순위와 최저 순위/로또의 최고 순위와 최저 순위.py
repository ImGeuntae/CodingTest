def solution(lottos, win_nums):
    ans1 = len(set(lottos) & set(win_nums))
    ans2 = ans1 + lottos.count(0)
    return [min(6,7-ans2),min(6,7-ans1)]