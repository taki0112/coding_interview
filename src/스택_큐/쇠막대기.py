def solution(arrangement):
    answer = 0
    left_bracket = []
    before = ''
    for bracket in arrangement :

        if bracket is '(' :
            left_bracket.append(bracket)
        else :
            left_bracket.pop(-1)

            if before is '(' :
                answer += len(left_bracket)
            else :
                answer += 1
        before = bracket
    return answer

arrangement = "(((()(()()))(())()))(()())"
x = solution(arrangement)
print(x)