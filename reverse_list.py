A=[20,40,50,800,900]
################### using Loops ######################
rev_list=[]
n=len(A)
print(n)
for i in range(n-1,-1,-1):
    print(A[i])
    rev_list.append(A[i])
print(rev_list)

################### Using list methods ###########################
A.reverse()
print(A)

###################### using slicing ############################
print(A[::-1])

