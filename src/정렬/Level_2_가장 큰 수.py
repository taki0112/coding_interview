
def solution(numbers):
    numbers = list(map(str, numbers))
    max_len = max([len(x) for x in numbers])
    numbers.sort(key=lambda x: x*max_len, reverse=True)
    return str(int(''.join(numbers)))


numbers = [9, 95, 9, 82, 9, 813]
x = solution(numbers)

print(x)