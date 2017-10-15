input1 = list(map(int,input("").split(" ")))
A = list(map(int,input("").split(" ")))
N = input1[0]
M = input1[1]
temp = [ input() for _ in range(M) ]
XY = [None] * M
for i in range(M):
 	XY[i] = list(map(int,temp[i].split(" ")))

for j in range(M):
	A[XY[j][0]-1] = XY[j][1]
	sorted(A, reverse=True)
	magic = [None] * N
	for ball in A:
		index = 1
		while (ball-index) >= 0:
			if magic[ball-index] == None:
				magic[ball-index] = ball
				break
			elif magic[ball-index] == ball:
				index += 1
			else:
				break
	print(magic.count(None))