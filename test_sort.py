#l = [(5, 2, 1,2),(5,2,2,1),(4,3,1,2),(5,3,2,1),(5,3,1,4)]

#l.sort(key=lambda x: (x[0], x[1], x[3],x[2]), reverse=True)
#print(l)

#print(int(5.98))
N = 4
rotate = [[(i,j) for i in range(N)] for j in range(N-1, -1,-1)]
for r in rotate:
    print(r)

print(not 2)


stack= [5,2,3,14]
temp_stack = [[0]*4]
temp_stack.append(stack)
print(temp_stack)