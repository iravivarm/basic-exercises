li=["20","Data","pandas","python","locustus", "fox", "tiger"]
res=[]
for i,x in enumerate(li):
    if i not in(0,4,5):
        res.append(x)
print(res)
