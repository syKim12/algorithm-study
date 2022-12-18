def solution(number, k):
    answer = ''
    numlist = list(map(int, number))
    numlist2 = numlist.copy()
    numlist2.sort()
    for i in range(k):
        numlist.remove(numlist2[i])
    print(numlist)
    print(numlist2)
    for i in numlist:
        answer += str(i)
    return answer