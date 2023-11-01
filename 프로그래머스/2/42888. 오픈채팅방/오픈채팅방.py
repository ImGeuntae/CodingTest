def solution(record):
    UID = dict()
    result = []
    for i in record:
        if i[0] in ["E","C"]:
            *_, uid, name = i.split()
            UID[uid] = name
            if i[0] == "E":
                result.append("E"+uid)
        elif i[0] == "L":
            *_, uid = i.split()
            result.append("L"+uid)
    return [UID[x[1:]]+"님이 들어왔습니다." if x[0]=="E" else UID[x[1:]]+"님이 나갔습니다."for x in result]
    