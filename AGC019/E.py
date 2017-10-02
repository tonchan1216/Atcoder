import re

A = input("")
B = input("")
k = A.count('1')

def find1(text):
	pattern = r"1"
	iterator = re.finditer(pattern ,text)
	temp = []
	for match in iterator:
		temp.append(match.start() + 1)
	return temp

a = find1(A)
b = find1(B)
hd = int(bin(int(A,2)^int(B,2)).count('1')/2)
both1 = bin(int(A,2)&int(B,2)).count('1')
num = 0
for p in range(hd+1):
	for q in range(hd-p,both1+1):
		r = both1 - q
		print("p:" + str(p) + ",q:" + str(q) + ",r:" + str(r))