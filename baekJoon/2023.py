def debug(ls):
    #print("##########")
    for l in ls:
        print(l)
    return

def check_sosu(num):
    stop_num = num // 2
    for i in range(2,stop_num+1):
        if num % i == 0 and num != i:
            return False
    return True


def dfs(str_num):
    #print(str_num)
    if check_sosu(int(str_num)): 
        #print("소수: ", str_num)
        if len(str_num) == length:
            ans.append(str_num)
            return 
        for i in range(1,10,2): # 홀수만 더함
            dfs(str_num + str(i))

def main():
    global length, ans
    length = int(input())
    ans = []
    for i in range(2,10):
        dfs(str(i))
    debug(ans)

main()