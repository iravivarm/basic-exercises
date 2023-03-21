from itertools import permutations
perm=permutations([2,4,5,6])
count=0
for i in perm:
    print(i)
    count += 1
print(count)