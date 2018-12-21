from itertools import permutations

def solution(numbers):
    answer = 0
    candidates, num_set = [], set()
    digits = [digit for digit in numbers]

    for i in range(1, len(numbers)+1):
        candidates += [*list(permutations(digits, i))]

    for candidate in candidates:
        num_set.add(int(''.join(map(str, candidate))))

    for num in num_set:
        if is_prime(num):
            answer += 1

    return answer

def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number//2 + 1):
        if (number/i) == (number//i):
            return False

    return True

numbers = "011"
x = solution(numbers)
print(x)