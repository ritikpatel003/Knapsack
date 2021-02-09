n = 5
arr=[2,5,3,7,11]
diff = 3

w = (sum(arr)+diff)//2-diff

dp=[[0 for i in range(w+1)] for i in range(n+1)]
for i in range(n+1):
	dp[i][0]=1

for i in range(1,n+1):
	for j in range(1,w+1):
		if j-arr[i-1]>=0:
			dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j]
		else:
			dp[i][j]=dp[i-1][j]

print(dp[-1][-1])
