from collections import deque
#현재값에서 어떤 문제를 풀어야하는지 구함
def dfs(nalp, ncop, ntime, problems, nproblems):
    for i in range(len(problems)):
        if (nalp >= problems[i][0]) and (ncop >= problems[i][1]):
            continue
        else:
            break
        return ntime
    q = deque(problems)
    alp_max = 1e9
    cop_max = 1e9
    fin_alp, fin_cop, fin_time = 0, 0, 0
    while q:
        alp, cop, qalp, qcop, qtime = q.popleft()
        #if nalp >= alp and ncop >= cop:
        #    nproblems.append([qalp, qcop, qtime])
        #    continue
        dalp = alp - nalp
        dcop = cop - ncop
        #print(dalp, dcop, nalp)
        if dalp > dcop:
            kalp = dalp//qalp
            if kalp < alp_max:
                alp_max = kalp
                fin_alp, fin_cop, fin_time = qalp, qcop, qtime
            elif kalp == alp_max:
                if qtime < fin_time:
                    fin_alp, fin_cop, fin_time = qalp, qcop, qtime
        #cop의 차이가 더 클때
        elif dalp < dcop:
            kcop = dcop//qcop
            if kcop < cop_max:
                cop_max = kcop
                fin_alp, fin_cop, fin_time = qalp, qcop, qtime
            elif kcop == cop_max:
                if qtime < fin_time:
                    fin_alp, fin_cop, fin_time = qalp, qcop, qtime
        else:
            kalp = dalp//qalp
            kcop = dcop//qcop
            if kalp > kcop:
                if kalp < alp_max:
                    alp_max = kalp
                    fin_alp, fin_cop, fin_time = qalp, qcop, qtime
                elif kalp == alp_max:
                    if qtime < fin_time:
                        fin_alp, fin_cop, fin_time = qalp, qcop, qtime
            elif kalp < kcop:
                if kcop < cop_max:
                    cop_max = kcop
                    fin_alp, fin_cop, fin_time = qalp, qcop, qtime
                elif kcop == cop_max:
                    if qtime < fin_time:
                        fin_alp, fin_cop, fin_time = qalp, qcop, qtime
            else:
                if qtime < fin_time:
                    fin_alp, fin_cop, fin_time = qalp, qcop, qtime
    #dalp, dcop = fin_alp - nalp, fin_cop - ncop
    #n1 = dalp//fin_alp
    #n2 = dcop//fin_cop
    if alp_max <= cop_max:
        nalp += alp_max*fin_alp
        ncop += alp_max*fin_cop
        ntime += alp_max*fin_time
    elif alp_max > cop_max:
        nalp += cop_max * fin_alp
        ncop += cop_max * fin_cop
        ntime += cop_max * fin_time
    """
    #같을때
    else:
        #n = min(alp_max, n2)
        nalp += n * fin_alp
        ncop += n * fin_cop
        ntime += n * fin_time
        """
    #new = [fin_alp, fin_cop, fin_time]
    #for k in nproblems:
    #    if k[0] != new[0] and k[1] != new[1] and k[2] != new[2]:
    #        nproblems.append([fin_alp, fin_cop, fin_time])
    #        break
    #print(nproblems)
    return dfs(nalp, ncop, ntime, problems, nproblems)

#def bfs




def solution(alp, cop, problems):
    nproblems = [[1, 0, 1], [0, 1, 1]]
    answer = dfs(alp, cop, 0, problems, nproblems)
    return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))