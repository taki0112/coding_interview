def solution(brown, red):
    size = brown + red
    answer = []

    x = []

    for n in range(1, size+1) :
        if size % n == 0 :
            if n >= size // n :
                x.append([n, size // n])


    for candidate in x :
        height, width = candidate[0], candidate[1]

        if (height - 2) * (width - 2) == red and (height + width)*2 - 4 == brown :
            answer = [height, width]

    return answer

brown = 24
red = 24

x = solution(brown, red)
print(x)