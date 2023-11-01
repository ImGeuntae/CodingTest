def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    A = [sum([n%i for n in data[i-1]]) for i in range(row_begin,row_end+1)]
    answer = A[0]
    for i in range(len(A)-1):
        answer = answer ^ A[i+1]
    return answer