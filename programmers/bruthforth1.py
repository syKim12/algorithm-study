def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    p1 = len(answers)//5
    q1 = len(answers)%5
    p2 = len(answers)//8
    q2 = len(answers)%8
    p3 = len(answers)//10
    q3 = len(answers)%10
    
    s1_fin = s1*p1 + [s1[i] for i in range(q1)]
    s2_fin = s2*p2 + [s2[i] for i in range(q2)]
    s3_fin = s3*p3 + [s3[i] for i in range(q3)]
    
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1_fin[i]:
            cnt[0] += 1
        if answers[i] == s2_fin[i]:
            cnt[1] += 1
        if answers[i] == s3_fin[i]:
            cnt[2] += 1
          
    answer = []
    
    
     
    return answer