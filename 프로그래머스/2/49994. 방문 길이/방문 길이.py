def solution(dirs):
    x = y = 0
    answer = set()
    for i in dirs:
        if (i == "L" and x != -5):
            answer.add((x-0.5,y))
            x -= 1
        elif (i == "R" and x != 5):
            answer.add((x+0.5,y))
            x += 1
        elif (i == "U" and y != 5):
            answer.add((x,y+0.5))
            y += 1
        elif (i == "D" and y != -5):
            answer.add((x,y-0.5))
            y -= 1
    return len(answer)