A=[5,6,-1,7,8]
dp = [0 for i in range(len(A))]
dp[0]=A[0]
for i in range(len(A)):
    dp[i]=