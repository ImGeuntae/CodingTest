def solution(want, number, discount):
    return sum([1 for i in range(len(discount)-9) if not [True for w,n in zip(want,number) if discount[i:i+10].count(w) < n]])