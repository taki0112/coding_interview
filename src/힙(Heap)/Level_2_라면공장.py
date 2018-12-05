import heapq

def solution(stock, dates, supplies, k):
    answer, start = 0, 0
    x = []
    n = len(dates)

    while stock < k:
        for i in range(start, n):
            if dates[i] <= stock:
                heapq.heappush(x, -supplies[i])
            else:
                start = i
                break
        answer += 1
        stock += -heapq.heappop(x)
        
    return answer