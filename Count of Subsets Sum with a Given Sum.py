nums = [3,5,6,7,4]
target = 9
dp=[[0 for i in range(target+1)] for i in range(len(nums)+1)]
for i in range(len(nums)+1):
	dp[i][0]=1
for i in range(1,len(nums)+1):
	for j in range(1,target+1):
		if j-nums[i-1]>=0:
			dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j]
		else:
			dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
