from math import ceil

def solution(progresses, speeds):
    answer = []

    max_time = ceil((100 - progresses[0]) / speeds[0])
    n = 1
    
    for i in range(1, len(progresses)) :
        time = ceil((100 - progresses[i]) / speeds[i])

        if max_time < time :
            answer.append(n)

            n = 1
            max_time = time
        else :
            n += 1

    answer.append(n)

    return answer


progresses = [93,30,55]
speeds = [1,30,5]

x = solution(progresses, speeds)
print(x)