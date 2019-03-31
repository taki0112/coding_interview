def solution(number, k):
    start = 0

    for i in range(k) :

        isEnd = True
        for j in range(start, len(number) - 1) :

            if number[j] < number[j + 1] :
                number = number[ : j] + number[j + 1 : ]
                isEnd = False
                if j > 0 :
                    start = j - 1
                else :
                    start = 0
                break

        if isEnd == True :
            number = number[ : -1]
            start = j - 1

    return number


number = "4177252841"
k = 4

x = solution(number, k)
print(x)