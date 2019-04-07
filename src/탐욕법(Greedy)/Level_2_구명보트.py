def solution(people, limit):
    people.sort()
    num_people = len(people)

    light = 0
    heavy = num_people - 1

    pair = 0

    while light < heavy :

        if people[light] + people[heavy] <= limit:

            pair += 1
            light, heavy = light + 1, heavy - 1

        else:
            heavy -= 1

    return num_people-pair



people = [70, 50, 80, 50]

limit = 100

x = solution(people, limit)
print(x)