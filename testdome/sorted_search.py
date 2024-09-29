def count_numbers(sorted_list, less_than):
    idx = 0
    while 0<= idx < len(sorted_list):
        idx = (idx+len(sorted_list))//2
        if idx == len(sorted_list)-1:
            if sorted_list[idx-1] <= less_than and sorted_list[idx]>less_than:
                return idx + 1
        if idx == 0:
            return 0
        if sorted_list[idx] <= less_than and sorted_list[idx+1]>less_than:
            return idx +1
        else:
            if sorted_list[idx]<less_than:
                idx = (idx + len(sorted_list))//2
            elif sorted_list[idx] > less_than:
                idx = idx // 2
    return 0

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2



def count_numbers(sorted_list, less_than):
    if len(sorted_list) == 0:
        return 0
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if mid == len(sorted_list) - 1:
            if mid <= less_than:
                return mid + 1
            else:
                return mid - 1
        if sorted_list[mid] < less_than and sorted_list[mid+1] > less_than:
            return mid + 1
        elif sorted_list[mid] > less_than:
            end = mid - 1
        elif sorted_list[mid] < less_than:
            start = mid + 1
    return 0

if __name__ == "__main__":
    sorted_list = [3, 5, 7, 8, 9, 11]
    sorted_list.sort()
    print(count_numbers(sorted_list, 2)) # should print 2


def count_numbers(sorted_list, less_than):
    if len(sorted_list) == 0:
        return 0
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if sorted_list[mid] == less_than:
            return mid
        
        elif sorted_list[mid] > less_than:
            if mid > 0:
                if sorted_list[mid-1] < less_than:
                    return mid
            else:
                end = mid - 1
        elif sorted_list[mid] < less_than:
            if mid < len(sorted_list)-1:
                if sorted_list[mid+1] >= less_than:
                    return mid+1
            else:
                start = mid + 1
    return 0

if __name__ == "__main__":
    sorted_list = [3, 5, 7, 8, 9, 11]
    sorted_list.sort()
    print(count_numbers(sorted_list, 2)) # should print 2


#######
def count_numbers(sorted_list, less_than):
    if len(sorted_list) == 0:
        return 0
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if sorted_list[mid] == less_than:
            return mid
        if sorted_list[mid] < less_than:
            if mid < len(sorted_list)-1:
                if sorted_list[mid+1] < less_than:
                    start = mid + 1
            else:
                return mid+1
        if sorted_list[mid] > less_than:
            if mid == 0:
                return 0
            elif sorted_list[mid-1] < less_than:
                    return mid
            else:
                end = mid - 1
  
    return 0

if __name__ == "__main__":
    sorted_list = [3, 5, 7, 8, 9, 11]
    sorted_list.sort()
    print(count_numbers(sorted_list, 2)) # should print 2



def count_numbers(sorted_list, less_than):
    if len(sorted_list) == 0:
        return 0
    if sorted_list[len(sorted_list)-1] < less_than:
        return len(sorted_list)
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if sorted_list[mid] == less_than:
            return mid
        if sorted_list[mid] < less_than:
            if mid < len(sorted_list)-1:
                if sorted_list[mid+1] < less_than:
                    start = mid + 1
                    continue
            else:
                return mid+1
        if sorted_list[mid] >= less_than:
            end = mid - 1
        else:
            start = mid + 1
    return 0

if __name__ == "__main__":
    sorted_list = [3, 5, 7, 8, 9, 11]
    sorted_list.sort()
    print(count_numbers(sorted_list, 2)) # should print 2