def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)) :
        if citations[i] < i+1 :
            return i
    else :
        return len(citations)

citations = [3, 0, 6, 1, 5]
x = solution(citations)

print(x)