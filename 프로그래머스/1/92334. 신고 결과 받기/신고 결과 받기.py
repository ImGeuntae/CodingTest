def solution(id_list, report, k):
    id_list, mail_list = dict.fromkeys(id_list,0), dict.fromkeys(id_list,"")
    report = list(set(report))
    for i in report:
        a,b = i.split(" ")
        id_list[b] += 1
        mail_list[a] += (b + " ")
    answer = []
    for key,value in mail_list.items():
        answer.append(len([x for x in value.split(" ")[:-1] if id_list[x] >= k]))
    return answer