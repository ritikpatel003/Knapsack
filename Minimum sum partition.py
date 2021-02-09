N = 3
arr = [29, 24, 16]
s = sum(arr)
print(s)
w = s//2

dp=[[0 for i in range(w+1)] for j in range(N+1)]
for i in range(N+1):
	dp[i][0]=1

for i in range(1,N+1):
	for j in range(1,w+1):
		if j-arr[i-1]>=0:
			dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
		else:
			dp[i][j]=dp[i-1][j]
c=w
for i in dp[-1][::-1]:
	if i==1:
		print(s-2*c)
		break
	c-=1