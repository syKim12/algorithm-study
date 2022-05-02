def solution(numbers, hand):
    answer = ''
    nl = (3, 0)
    nr = (3, 2)
    for k in numbers:
        if k in [1, 4, 7]:
            answer += 'L'
            if k == 1:
                nl = (0, 0)
            elif k == 4:
                nl = (1, 0)
            else:
                nl = (2, 0)
        elif k in [3, 6, 9]:
            answer += 'R'
            if k == 3:
                nr = (0, 2)
            elif k == 6:
                nr = (1, 2)
            else:
                nr = (2, 3)
        else:
            if k == 2:
                current = (0,1)
            elif k == 5:
                current = (1,1)
            elif k == 8:
                current = (2, 1)
            else:
                current = (3,1)
            ldist = abs(nl[0]-current[0]) + abs(nl[1]-current[1])
            rdist = abs(nr[0]-current[0]) + abs(nr[1]-current[1])
            if ldist < rdist:
                answer += 'L'
            
                    
            
    return answer