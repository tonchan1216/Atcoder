import numpy as np
from scipy import stats

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
	mode = stats.mode(top)
	count = len(np.where(top == mode)[0])
	if result > count:
		result = count

	for i in range(N):
		temp = np.delete(A[i], np.where(A[i] == mode)[0])
		A[i] = np.append(temp,0)

print(result)