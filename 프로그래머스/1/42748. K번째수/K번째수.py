def solution(array, commands):
    answer = []
    for i in commands:
        num_list = sorted(array[i[0]-1:i[1]])
        answer.append(num_list[i[2]-1])
    return answer