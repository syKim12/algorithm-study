#binary search
#시간복잡도 O(logN)
#처리할 데이터 개수나 값이 1,000만 단위 이상으로 넘어가면 이진탐색을 떠올리는게 도움됨

#재귀문으로 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

#반복문으로 구현
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid]==target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

#빨리 입력 받는 방법
import sys 
input_data = sys.stdin.readline().rstrip()

#binary search example
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
n = int(input())
array = list(map(int, input().split()))
array.sort()#이진 탐색을 위해 사전에 정렬 수행
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')