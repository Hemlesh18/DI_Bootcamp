list1 = [5, 10, 15, 20, 25, 50, 20]
i=list1.index(20)
list1=list1[:i]+[200]+list1[i+1:]
print(list1)


my_tuple = (10, 20, 30, 40)
a, b, c, d =my_tuple
print(a)
print(b)
print(c)
print(d)