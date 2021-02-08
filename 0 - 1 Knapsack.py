n = 4
W = 4
val = [1,2,3,4]
wt = [4,5,1,2]
dp=[[0 for i in range(n+1)] for j in range(W+1)]
for i in range(1,n+1):
	for j in range(1,W+1):
		if j-wt[i-1]>=0:
			dp[j][i]=max(val[i-1]+dp[j-wt[i-1]][i-1],dp[j][i-1])
		else:
			dp[j][i]=dp[j][i-1]
print(dp[-1][-1])