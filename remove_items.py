list1 = [5, 20, 15, 20, 25, 50, 20]
k=list1.copy()
print(k)


for i in list1:
    if i == 20:
        list1.remove(i)
print(list1)

while 20 in list1:
    list1.remove(20)
print(list1)

