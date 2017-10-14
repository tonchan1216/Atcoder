input1 = list(map(int,input("").split(" ")))
N = input1[0]
A = input1[1]
B = input1[2]
C = input1[3]
D = input1[4]

flag = False
for x in range(N-1):
	y = N -1 - x
	if (C*y - D*x) <= (B-A) and (B-A) <= -1*C*x + y*D:
		flag = True
		break

if flag == True:
	print('YES')
else:
	print('NO')