a=[1,2,3,4]
count=0
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if i!=j and j!=k and k!=i:
                print(a[i],a[j],a[k])
                count+=1
print(count)