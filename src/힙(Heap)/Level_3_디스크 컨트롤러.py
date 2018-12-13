import heapq

def solution(jobs):
    pool = []

    elapsted_t = 0
    current_t = 0
    initial_t = 0

    n = len(jobs)

    heapq.heapify(pool)

    jobs = sorted(jobs, key=lambda x: x[0])

    while jobs or pool :
        while jobs :
            if current_t >= jobs[0][0]:
                st, et = jobs.pop(0)
                initial_t += st
                heapq.heappush(pool, et)

            else:
                break

        if pool :
            et = heapq.heappop(pool)
            current_t += et
            elapsted_t += current_t

        else:
            current_t = jobs[0][0]

    answer = (elapsted_t-initial_t) // n

    return answer


jobs = [[1, 9], [0, 3], [2, 6]]

x = solution(jobs)
print(x)