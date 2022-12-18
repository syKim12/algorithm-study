def findMin(d):
  curr = d[2]
  rst = 2
  if d[1] <= curr:
    curr = d[1]
    rst = 1
  if d[0] <= curr:
    curr = d[0]
    rst = 0
  return rst
 
def binary(item, B, start, end):
  diff = end - start
  if diff <= 1:
    return start
  mid = (start + end) // 2
  if item < B[mid]:
    return binary(item, B, start, mid)
  else: # item >= B[mid]
    return binary(item, B, mid, end)
 
def solve():
  n, m = [int(x) for x in input().split()]
  A = [int(x) for x in input().split()]
  B = [int(x) for x in input().split()]
  B.sort()
  s = 0
  for item in A:
    p = binary(item, B, 0, m)
    d = []
    d.append(abs(B[p-1] - item))
    d.append(abs(B[p] - item))
    d.append(abs(B[(p+1)%m] - item))
    idx = findMin(d)
    s += B[p + idx - 1]
  print(s)
 
t = int(input())
for _ in range(t):
  solve()
