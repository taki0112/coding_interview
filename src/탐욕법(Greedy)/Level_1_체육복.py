def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]


    for r in _reserve:
        f = r - 1
        b = r + 1

        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    x = n - len(_lost)

    return x

n = 5
lost = [2, 4]
reserve = [3]

x = solution(n, lost, reserve)
print(x)