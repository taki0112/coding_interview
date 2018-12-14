def solution(operations):
    x = []
    for op in operations :
        order, num = op.split()[0], int(op.split()[1])

        if order == 'I' :
            x.append(num)
        if order == 'D' :
            try :
                if num == 1 :
                    x.remove(max(x))
                if num == -1 :
                    x.remove(min(x))
            except ValueError :
                continue

    if not x :
        answer = [0, 0]
    else :
        answer = [max(x), min(x)]

    return answer


operations = ["I 7", "I 5", "I -5", "D -1"]
# operations = ["I 7", "D 1", "D 1", "D -1"]
x = solution(operations)

print(x)