def solution(N):

    x = [1, 1]

    for i in range(2, N):
        x.append(x[i - 1] + x[i - 2])

    answer = ((x[N-1] + x[N-2]) + (x[N-2] + x[N-3])) * 2

    return answer

x = solution(6)
print(x)