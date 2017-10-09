import numpy as np

A = np.array([[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3]])
N = 4
mode = 5
for i in range(N):
	temp = np.delete(A[i], np.where(A[i] == mode)[0])
	temp = np.append(temp,0)
	print(temp)