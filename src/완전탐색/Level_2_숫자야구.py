from itertools import permutations

def get_strike_ball(number, candidate_number):
    strike = 0
    ball = 0

    number_difference = []
    candidate_difference = []

    for i in range(3):
        if number[i] == candidate_number[i]:
            strike += 1
        else:
            number_difference.append(number[i])
            candidate_difference.append(candidate_number[i])

    for num in candidate_difference:
        if num in number_difference:
            ball += 1

    return strike, ball


def solution(baseball):
    candidate = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

    x = []

    for example in baseball:

        number = [int(i) for i in str(example[0])]
        strike_ball = (example[1], example[2])

        for candidate_number in candidate:
            if get_strike_ball(number, candidate_number) == strike_ball:
                x.append(candidate_number)

        candidate = x
        x = []

    return len(candidate)

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

x = solution(baseball)
print(x)