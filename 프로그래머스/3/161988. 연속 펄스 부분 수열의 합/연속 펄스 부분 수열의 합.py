def solution(sequence):
    A, B = [0], [0] 
    for a,b in [(n,-n) if (idx%2) else (-n,n) for idx,n in enumerate(sequence)]:
        A.append(max(a,a+A[-1]))
        B.append(max(b,b+B[-1]))
    return max(max(A),max(B))