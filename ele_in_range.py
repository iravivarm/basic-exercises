a=[2,3,4,8,9,10,11,12,14]
x,y=2,13
res=True
for i in a:
    if x < i or i >= y:
        print("list is out of range")
        res=False
print(res)