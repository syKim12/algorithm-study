"""
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
"""
#수정
def solution(citations):
    answer = 0
    n = max(citations)
    maxn = 0
    citations.sort()
    for h in range(0, n+1):
        for i in range(1,len(citations)):
            if i == 1 and citations[i-1] >= h:
                if len(citations[i-1:]) >= h:
                    #print(maxn, h)
                    maxn = max(maxn, h)
            if citations[i-1] <= h and citations[i] >= h:
                
                if len(citations[i:]) >= h and len(citations[:i]) <= h:
                    maxn = max(maxn, h)
                    #print("2",i,h)
    answer = maxn  
    return answer