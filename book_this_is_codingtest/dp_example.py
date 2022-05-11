#1로 만들기
x = int(input())

d= [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    print(d)
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d)
print(d[x])

"""5를 입력하면
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 2, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 2, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 2, 3, 0, 0, 0, 0]
[0, 0, 1, 1, 2, 1, 0, 0, 0, 0]
위와 같이 나온다
d에는 각 숫자를 만드는 최소 횟수가 적혀있다.
"""

#개미 전사
n = int(input())
array = list(map(int, input().split()))

d = [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1] + d[i-2]+array[i])
print(d[n-1])

#바닥 공사
n = int(input())

d = [0]*1001
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2])%796796
print(d[n])

#효율적인 화폐 구성
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001: #(i-k) 원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
