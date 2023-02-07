def sol(n):
    value = N // 5
    bags = value
    for num in range(value, -1, -1):
        value_3 = (N-num*5) // 3
        remain_3 = (N-num*5) % 3
        if remain_3 == 0:
            print(bags + value_3)
            return
        bags -= 1
    print(-1)
    return

N = int(input())
sol(N)

    
