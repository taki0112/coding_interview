def solution(N, number):
    num_set = []


    num_set.append([N])
    for i in range(2, 9) :
        lst = [int(str(N)*i)]

        max_num = int(i / 2)

        for X_index in range(0, max_num) :
            Y_index = i - X_index - 2

            X = num_set[X_index]
            Y = num_set[Y_index]

            for x in X :
                for y in Y :
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)

                    if x != 0 :
                        lst.append(int(y / x))
                    if y != 0 :
                        lst.append(int(x / y))

        if number in set(lst) :
            return i

        num_set.append(lst)

    return -1


N = 5
number = 12

x = solution(N, number)
print(x)