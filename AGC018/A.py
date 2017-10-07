def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

input1 = list(map(int,input("").split(" ")))
A = list(map(int,input("").split(" ")))
N = input1[0]
K = input1[1]

temp = A[0]
for i in range(1,N):
	temp = gcd(temp,A[i])

if K <= max(A) and K % temp == 0:
	print('POSSIBLE')
else:
	print('IMPOSSIBLE')