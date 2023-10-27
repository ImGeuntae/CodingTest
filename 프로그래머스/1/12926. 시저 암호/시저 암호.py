def solution(s, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join([alphabet[(alphabet.index(x)+n)%26] if x.islower() else (alphabet[(alphabet.index(x.lower())+n)%26]).upper() if x.isupper() else " "for x in s])
    