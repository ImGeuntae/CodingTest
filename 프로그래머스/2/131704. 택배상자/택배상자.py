def solution(order):
    belt = list(range(len(order),0,-1))
    deque = []
    i = 0
    while i<len(order):
        if belt and order[i] == belt[-1]:
            belt.pop()
            i += 1
        elif deque and order[i] == deque[-1]:
            deque.pop()
            i += 1
        else:
            if belt:
                deque.append(belt.pop())
            else:
                return i
    return i