def solution(brown, yellow):
    answer = []
    sumnum = brown + yellow
    divnum = []
    for i in range(3, sumnum):
        if sumnum % i == 0:
            divnum.append([i, int(sumnum/i)])
    for k in divnum:
        if brown == 2*(k[0]+k[1])-4 and yellow == (k[0]-2)*(k[1]-2):
            answer=k

    return answer