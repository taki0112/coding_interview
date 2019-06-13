

def solution(weight):
    weight.sort()

    answer = 1

    for w in weight:

        if answer < w:
            break

        answer += w

    return answer


weight = [3, 1, 6, 2, 7, 30, 1]


x = solution(weight)
print(x)