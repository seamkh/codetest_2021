a = [1,5,4,6,8,11,3,12]
even = list(filter(lambda x:(x%2 == 0),a))
print(even)
ten_times = list(map(lambda x:x*10,a))
print(ten_times)

b = [[0,1,8],[7,2,2],[5,3,0],[1,4,5]]
b.sort(key = lambda x:x[2])
print(b)
