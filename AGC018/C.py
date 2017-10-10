input1 = input("").split(" ")
X = int(input1[0])
Y = int(input1[1])
Z = int(input1[2])
N = X + Y + Z
temp = [ input() for _ in range(N) ]
matrix = [None]*N
for i in range(N):
	a = int(temp[i].split(" ")[0])
	b = int(temp[i].split(" ")[1])
	c = int(temp[i].split(" ")[2])
	matrix[i] = [i, a, b, c, (a-b), (b-c), (c-a)]

###########################################
matrix.sort(key=lambda k: k[4])
result = 0
for k in range(Y,N-X):
	temp1 = sorted(matrix[:k], key=lambda k: k[5], reverse=True)
	temp1 = list(map(list, zip(*temp1)))
	temp2 = sorted(matrix[k:], key=lambda k: k[6], reverse=True)
	temp2 = list(map(list, zip(*temp2)))

	coins =	sum(temp1[2][:Y]) +	sum(temp1[3][Y:]) +	sum(temp2[3][:(N-k-X)]) + sum(temp2[1][(N-k-X):])
	if result < coins:
		result = coins

print(result)