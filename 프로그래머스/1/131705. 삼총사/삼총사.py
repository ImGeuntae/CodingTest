from itertools import combinations as c
def solution(number):
    return sum([1 for i in c(number,3) if sum(i) == 0])