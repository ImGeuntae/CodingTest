def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    A = [sum([n%i for n in data[i-1]]) for i in range(row_begin,row_end+1)]
    answer = 0
    for i in A:
        answer = answer ^ i
    return answer