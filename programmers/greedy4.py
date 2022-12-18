from itertools import combinations

def solution(people, limit):

    comb = list(combinations(people, 2))
    comb_list = [list(i) for i in comb]
    result=[]
    for k in comb_list:
        if sum(k) <= limit:
            result.append(k)
    if len(result) >= len(people):
        answer = len(people)/2
    else:
        boat_for_2 = len(result)
        boat_for_1 = len(people) - 2*boat_for_2
        answer = boat_for_2+boat_for_1
    
    return answer