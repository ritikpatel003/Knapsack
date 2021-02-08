n = 4
W = 4
val = [1,2,3,4]
wt = [4,5,1,2]
def sol(n,w):
	if n==0:
		return 0
	if w-wt[n-1]>=0:
		return max(val[n-1]+sol(n-1,w-wt[n-1]),sol(n-1,w))
	else:
		return sol(n-1,w)

print(sol(n,W))
