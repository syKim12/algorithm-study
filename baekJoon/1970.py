T = int(input())

for t in range(1, T+1) :
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    list = [0] * 8
    for i in range(8) :
        if N//money[i] != 0 :
            list[i] = N//money[i]
            N = N%money[i]
    print("#{}".format(t))
    print(*list)