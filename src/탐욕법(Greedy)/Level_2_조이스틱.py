def solution(name):
    updown = list(range(14)) + list(range(12,0,-1))

    updown = {chr(65+k):v for k, v in enumerate(updown)}

    name = [updown[x] for x in name]

    right = 0
    left = 0

    for i in range(len(name)-1):
        if name[1+i] != 0:
            break
        right += 1

    for i in range(len(name)-1):
        if name[-i-1] != 0:
            break
        left -= 1

    return sum(name) + len(name) - 1 - max(left, right)

name = 'JAZ'

x = solution(name)
print(x)