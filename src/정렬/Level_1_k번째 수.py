def solution(array, commands):
    answer = []
    for command in commands :
        start_index = command[0] - 1
        end_index = command[1]
        find_index = command[2] - 1

        x = array[start_index : end_index]
        x.sort()
        answer.append(x[find_index])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

x = solution(array, commands)
print(x)