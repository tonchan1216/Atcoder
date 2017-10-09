import numpy as np
from collections import Counter

input1 = input("").split(" ")
N = int(input1[0])
M = int(input1[1])
temp = [ input() for _ in range(N) ]
A = []
for i in range(N):
	A.append(list(map(int,temp[i].split(" "))))

A = np.array(A)
result = N

for j in range(M):
	top = A[:,0]
	c = Counter(list(top))
	most = c.most_common(1)
	mode = most[0][0]
	count = most[0][1]

	if result > count:
		result = count

	for i in range(N):
		temp = np.delete(A[i], np.where(A[i] == mode)[0])
		A[i] = np.append(temp,0)

print(result)