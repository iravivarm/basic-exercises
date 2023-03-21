A=[1,2,3,4,5,6,7]
##################### space 0(1), tc:O(N) ##################
for num in range(len(A)):
    A[num]=A[num]*A[num]
print(A)

##################### space 0(N), tc:O(N) ##################
sqr_num=[]
for num in range(len(A)):
   sqr_num.append(A[num]*A[num])
print(sqr_num)
