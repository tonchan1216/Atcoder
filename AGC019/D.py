A = input("")
B = input("")

def left(x):
	return x[1:] + x[0]

def right(x):
	return x[-1] + x[:-2]

def rev(x,y):
	return bin(int(x,2) ^ 1<<(len(x)-y+1))