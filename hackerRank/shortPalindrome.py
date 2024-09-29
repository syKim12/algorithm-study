def find_closest_numbers(l, num):
    low, high = 0, len(l) - 1
    closest_smaller, closest_larger = None, None

    while low <= high:
        mid = (low + high) // 2
        if l[mid] < num:
            closest_smaller = l[mid]  # num보다 작지만 가장 큰 수 저장
            low = mid + 1
        elif l[mid] > num:
            closest_larger = l[mid]  # num보다 크지만 가장 작은 수 저장
            high = mid - 1
        else:
            # num과 정확히 일치하는 경우 (중복 값 없다고 가정)
            break

    # num보다 작은 값들 중 최대값을 찾고, num보다 큰 값들 중 최소값을 찾습니다.
    return closest_smaller, closest_larger

# 예제 사용
l = [1, 3, 5, 7, 9, 11, 13, 15]
num = 10
result = find_closest_numbers(l, num)
print("Closest smaller:", result[0], "Closest larger:", result[1])
