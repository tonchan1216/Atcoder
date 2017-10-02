A = input("")
B = input("")

def left(x):
	return x[1:] + x[0]

def right(x):
	return x[-1] + x[:-2]

def rev(x,y):
	return bin(int(x,2) ^ 1<<(len(x)-y+1))

def hamming(x,y):
	return int(bin(int(x,2)^int(y,2)).count('1'))

if B.count('1') == 0:
	if A.count('1') == 0:
		num = 0
	else:
 		num = -1
else:
	num = 0
	target = A
