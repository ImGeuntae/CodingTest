def solution(book_time):
    book_time.sort(key=lambda x:(x[0],x[1]))
    room = {0:(0,0)}
    for x in book_time:
        x[0] = 60*int(x[0][:2]) + int(x[0][3:])
        x[1] = 60*int(x[1][:2]) + int(x[1][3:])
        for r, (i,o) in room.items():
            if (o <= x[0]):
                room[r] = (x[0],x[1]+10)
                break
        else:
            room[len(room)] = (x[0],x[1]+10)
    return len(room)