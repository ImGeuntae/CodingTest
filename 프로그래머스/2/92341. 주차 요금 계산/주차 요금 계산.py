from collections import defaultdict
def solution(fees, records):
    dic = defaultdict(int)
    no_out = dict()
    for i in records:
        time, number, direction = i.split()
        H, M = time.split(":")
        if direction == "IN":
            no_out[number] = True
            dic[number] += int(H)*60 + int(M)
        else:
            del no_out[number]
            dic[number] -= (int(H)*60 + int(M))
    for k,v in no_out.items():
        dic[k] -= 23*60+59
    answer = []
    for j in sorted(dic):
        if -dic[j] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (-((dic[j]+fees[0])//fees[2])*fees[3]))
    return answer
