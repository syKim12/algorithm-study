#[[100, 100, 500], [1000, 1000, 100]]
#[[10, 19, 800], [20, 39, 200], [100, 199, 500]]
#[[50, 1, 50], [100, 199, 100], [1, 1, 500]]

def solution(lotteries):    
    answer = 0
    win, buy, price = 0, 0, 0
    probability = 0
    for i in range(len(lotteries)):
        temp_win, temp_buy, temp_price = lotteries[i][0], lotteries[i][1], lotteries[i][2]
        temp__p = temp_win/(temp_buy+1)
        if temp_win >= temp_buy+1:
            temp__p = 1
        if temp__p > probability:
            probability = temp__p
            price = temp_price
            answer = i + 1
        elif temp__p == probability:
            if temp_price > price:
                price = temp_price
                answer = i + 1
    print(answer)
    return answer



solution([[100, 100, 500], [1000, 1000, 100]])
solution([[50, 1, 50], [100, 199, 100], [1, 1, 500]])