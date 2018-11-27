def solution(heights):
    answer = [0]*len(heights)

    for x in range(len(heights)-1, 0, -1):
        for y in range(x-1, -1, -1):
            if heights[x] < heights[y]:
                answer[x] = y+1
                break
    return answer


heights = [1,5,3,6,7,6,5]
x = solution(heights)
print(x)