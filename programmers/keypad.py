
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
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
                nr = (2, 2)
        elif k in [2,5,8,0]:
            if k == 2:
                current = (0,1)
            elif k == 5:
                current = (1,1)
            elif k == 8:
                current = (2, 1)
            elif k == 0:
                current = (3,1)
            ldist = abs(nl[0]-current[0]) + abs(nl[1]-current[1])
            rdist = abs(nr[0]-current[0]) + abs(nr[1]-current[1])
            if ldist < rdist:
                answer += 'L'
                nl = current
            elif ldist > rdist:
                answer += 'R'
                nr = current
            else:
                if hand == 'left':
                    answer += 'L'
                    nl = current
                else:
                    answer += 'R'
                    nr = current


    return answer