from collections import Counter

def solution(clothes):
    num_clothes_kind = Counter([kind for name, kind in clothes])

    x = [ num + 1 for num in num_clothes_kind.values() ]
    answer = 1

    for x_i in x :
        answer *= x_i
    answer -= 1

    return answer

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
x = solution(clothes)
print(x)