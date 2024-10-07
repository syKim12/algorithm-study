def solution(orders, course):
    answer = []
    result = set()
    s_ord = []
    for order in orders:
        temp = set()
        for char in order:
            temp.add(char)
        s_ord.append(temp)
    print(s_ord)
    for i in range(len(orders)):
        for j in range(i+1, len(orders)):
            temp = [ char for char in s_ord[i] & s_ord[j]]
            print(temp)
            if len(temp) in course:
                temp.sort()
                result.add(''.join(temp))
                
    answer = [result]
    answer.sort()
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])