keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys,values)))

result={}
for i in range(len(values)):
    result.update({keys[i]:values[i]})

print(result)

