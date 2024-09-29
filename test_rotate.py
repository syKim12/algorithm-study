l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
r = list(map(list, zip(*l[::-1])))
print(r)

r2 = list(map(list,zip(*l)))[::-1]
print(r2)

#시계방향
rotate = list(map(list, zip(*l[::-1])))

#반시계
rotate_reverse = list(map(list, zip(*l)))[::-1]