A=[4,6,8,10,12,8,11,5]

largest=A[0]
for i in range(len(A)):
    if A[i] > largest:
        largest=A[i]
print(largest)
