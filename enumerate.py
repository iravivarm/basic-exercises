a = [1, 2, 3]
b = [3, 2, 1]
count=[]
for i,j in  zip(a,b):
    alice_count=0
    bob_count=0
    if a[i] > b[j]:
        alice_count += 1
        count.append(alice_count)
    if a[i] < b[j]:
        bob_count +=1
        count.append(alice_count)
print(count)

