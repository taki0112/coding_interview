from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

x = solution(participant, completion)
print(x)

