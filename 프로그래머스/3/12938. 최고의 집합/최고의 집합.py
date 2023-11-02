def solution(n, s):
    return [s//n]*(n-(s%n)) + [(s//n)+1]*(s%n) if n <= s else [-1]