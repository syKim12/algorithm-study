import heapq
def solution(jobs):
    answer = 0
    hq = []
    for time, duration in jobs:
        heapq.heappush(hq, (time, duration))
    time = 0
    wait = 0
    length = len(hq)
    while hq:
        tm, dur = heapq.heappop(hq)
        if tm > time:
            time = tm + dur
            wait += dur
        else:
            temp = [(dur, tm)]
            while hq:
                temp_tm, temp_dur = heapq.heappop(hq)
                temp.append((temp_dur, temp_tm))
                if temp_tm > time:
                    break
            heapq.heapify(temp)
            shortest_tm, shortest_dur = heapq.heappop(temp)
            # add time
            wait += time - shortest_tm + shortest_dur
            time += shortest_dur
            # add temp values
            hq.extend(temp)
            heapq.heapify(hq)
            
    return wait//length

solution([[0, 3], [1, 9], [2, 6]])