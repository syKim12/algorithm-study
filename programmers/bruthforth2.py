#from https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0

import math
from itertools import permutations

def is_prime_number(n):
    """소수판별 함수"""
    if n==0 or n==1:                                # 0,1 은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):   # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
            if n % i == 0:                          # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False
        
        return True                                 # for문을 다 돌았는데도 False가 아니면 소수

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):              
        arr = list(permutations(numbers, i))        # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
        for j in range(len(arr)):                   # 생성한 list(arr) 길이만큼 for문 실행
            num = int(''.join(map(str,arr[j])))     # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
            if is_prime_number(num):                
                answer.append(num)                  # is_prime_number() 함수가 True일 경우 (= 소수일 경우) num 추가
    
    answer = list(set(answer))                      # 같은 값이 나올 수 있기 때문에 set()을 통해 중복값 제거
    return len(answer)
    

print(solution("17"))       # result : 3
print(solution("011"))      # result : 2