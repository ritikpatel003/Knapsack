N = 4
arr = [1, 5, 11, 5]
s = sum(arr)
if s%2!=0:
	print("No")
else:
	w = s//2
	dp=[[False for i in range(w+1)] for j in range(N+1)]
	for i in range(N+1):
		dp[i][0]=True
	for i in range(1,N+1):
		for j in range(1,w+1):
			if j-arr[i-1]>=0:
				dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
			else:
				dp[i][j]=dp[i-1][j]
	if (dp[-1][-1]):
		print("Yes")
	else:
		print("No")