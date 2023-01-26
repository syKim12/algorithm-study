"""
def merge_sort(unsorted_list):
    if len(unsorted_list) < 1:
        return unsorted_list
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    m_left = merge_sort(left)
    m_right = merge_sort(right)
    return merge(m_left, m_right)

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list
"""
"""
for i in range(N-1, 0, -1):
    for j in range(i):
        if member[j][0] > member[j+1][0]:
            member[j], member[j+1] = member[j+1], member[j]
"""
import sys

N = int(sys.stdin.readline())
member = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    member.append([int(age), name])
member.sort(key=lambda x: x[0])

for age, name in member:
    print(age, name)