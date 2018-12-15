from collections import defaultdict

def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    x = defaultdict(int)

    max_score = 0
    for i in range(len(answers)) :
        ans = answers[i]
        one_ans = one[i % len(one)]
        two_ans = two[i % len(two)]
        three_ans = three[i % len(three)]

        if ans == one_ans :
            x[1] += 1

            if max_score < x[1] :
                max_score = x[1]

        if ans == two_ans :
            x[2] += 1

            if max_score < x[2] :
                max_score = x[2]

        if ans == three_ans :
            x[3] += 1

            if max_score < x[3] :
                max_score = x[3]


    for key, value in x.items() :
        if max_score == value :
            answer.append(key)

    answer.sort()

    return answer

answers = [1, 3, 2, 4, 2]

x = solution(answers)
print(x)