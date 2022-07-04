#테스트 케이스 9번 error
def solution(citations):
    answer = 0
    n = max(citations)
    maxn = 0
    citations.sort()
    for h in range(0, n+1):
        for i in range(len(citations)-1):
            if citations[i] <= h and citations[i+1] >= h:
                #print(i, h)
                if len(citations[i+1:]) >= h and len(citations[:i+1]) <= h:
                    maxn = max(maxn, h)
                    #print("2",i,h)
    answer = maxn  
    return answer