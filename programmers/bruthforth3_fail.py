def solution(brown, yellow):
    answer = []
    if yellow > brown:
        brown, yellow = yellow, brown
        
    for nrow in range(3,int(brown/2)):
        for ncol in range(3,int(brown/2)):
            if (brown == 2*(ncol+nrow) - 4) and (yellow == (nrow-2)*(ncol-2)):
                answer.append(nrow)
                answer.append(ncol)
                break
                        
    if len(answer) > 2:
        answer = sorted(set(answer), reverse=True)
    return answer