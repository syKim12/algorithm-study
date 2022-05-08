#selection sort
#시간 복잡도 O(n^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #swap
    array[i], array[min_index] = array[min_index], array[i]
print(array)

#insertion sort
#시간 복잡도 O(n^2)
#데이터가 거의 정렬 되어 있을 때는 효율적
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)

#quick sort
#시간 복잡도 O(nlogn)
#이미 데이터가 정렬되어 있는 경우 느리게 작동, 최악의 경우에는 O(n^2) 
#but 라이브러리 통해 O(nlogn)이 보장되게 할 수 있음
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    #원소가 1개인 경우 종료
    if start >= end:
        return
    pivot = start #피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    #분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# quick sort (ver.easier to remember but slower)
def quick_sort2(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] #피벗은 첫번째 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x<=pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x> pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)
print(quick_sort2(array))


#count sort
#데이터 크기가 제한 되어 정수형태로 표현할 수 있을 때만 사용할 수 있음
#동일한 값을 가지는 데이터가 여러개 등장할 때 적합
#시간복잡도 O(N+K)

#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9]
#모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end = ' ') #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

#파이썬 라이브러리
array = [7, 5, 9, 0, 3, 1, 6, 2, 9]
result = sorted(array)

array.sort()

#key를 sort하는 경우
def setting(data):
    return data[1]
array = [('바나나', 2), ('당근', 3), ('사과', 5)]
result = sorted(array, key = setting)