def combinations(data, length):
    r = []
    def dfs(cur, pos):
        if len(cur) == length:
            r.append(cur)
        if pos == len(data):
            return
        if type(data) is list:
            for i in range(pos, len(data)):
                dfs(cur+[data[i]], i+1)
        else:
            for i in range(pos, len(data)):
                dfs(cur+data[i], i+1)
    if type(data) is list:
        dfs([], 0)
    else:
        dfs("", 0)
    return r

print(combinations([1,2,3,4],2))
print(combinations("abcd",2))

def combinations2(data, length):
    r=[]
    def dfs(cur, pos):
        if len(cur) == length:
            r.append(cur)
        if pos == len(data):
            return
        if type(data) is list:
            for i in range(pos, len(data)):
                dfs(cur+[data[i]], i+1)
        else:
            for i in range(pos, len(data)):
                dfs(cur + data[i], i+1)
    if type(data) is list:
        dfs([],0)
    else:
        dfs("", 0)
    return r

print(combinations2([1,3,9],2))
print(combinations2("soo",3))
















