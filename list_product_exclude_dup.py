a=[2,4,4,5,5,6,8,9]
l=[]
product=1
for i in a:
    if i not in l:
        product = product * i
        l.append(i)
print(product)