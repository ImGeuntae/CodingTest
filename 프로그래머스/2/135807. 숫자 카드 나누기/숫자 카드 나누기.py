def solution(arrayA, arrayB):
    gcdA = gcdB = A = B = 0
    for i in arrayA:
        while i:            
            gcdA,i = i, gcdA%i
    for j in arrayB:
        while j:            
            gcdB,j = j, gcdB%j
    if gcdA != 1 and not [1 for b in arrayB if not b%gcdA]:
        A = gcdA
    if gcdB != 1 and not [1 for a in arrayA if not a%gcdB]:
        B = gcdB
    return max(A,B)