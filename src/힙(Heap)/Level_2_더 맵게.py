import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True :
        if scoville[0] >= K:
            return answer
        elif len(scoville) == 1:
            return -1

        t1 = heapq.heappop(scoville)
        t2 = heapq.heappop(scoville)

        heapq.heappush(scoville, t1 + 2*t2)
        answer += 1

scoville = [9, 1, 2, 3, 10, 12]
K = 7
x = solution(scoville, K)
print(x)
