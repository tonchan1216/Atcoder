from math import pi

input1 = list(map(int,input("").split(" ")))
N = int(input(""))
src = {"x":input1[0],"y":input1[1]}
dist = {"x":input1[2],"y":input1[3]}

spring = []
for i in range(N):
	temp = list(map(int,input("").split(" ")))
	if (src['x'] <= temp[0]) and (temp[0] <= dist['x']) or (dist['x'] <= temp[0]) and (temp[0] <= src['x']):
		if (src['y'] <= temp[1]) and (temp[1] <= dist['y']) or (dist['y'] <= temp[1]) and (temp[1] <= src['y']):
			spring.append({'x':temp[0], 'y':temp[1]})

# 基礎点
path = (abs(src['x']-dist['x']) + abs(src['y']-dist['y'])) * 100
n = len(spring)
if n > 0:
	r = 10
	if src['x'] == dist['x'] or src['y'] == dist['y'] :
		#１直線半円あり
		path += r*pi - 2*r 
	else:
		#1/4円あり
		if (src['x']-dist['x'])*(src['y']-dist['y']) > 0:
			spring.sort(key=lambda k: k['x'])
		else:
			spring.sort(key=lambda k: k['x'], reverse=True)

		#最長路問題
		L = [None] * n
		L[0] = spring[0]['y']
		length = 1
		for i in range(1,n):
			if L[length-1] < spring[i]['y']:
				L[length] = spring[i]['y']
				length += 1
			else:
				# 2分木探査風
				start = 0
				last = length - 1
				while abs(last-start) > 0:
					j = int((start+length)/2)
					if spring[i]['y'] < L[j] :
						last = j
					else:
						start = j
				L[last] = spring[i]['y']
		
		#半円があるかないか	
		if length < min(abs(src['x']-dist['x']),abs(src['y']-dist['y'])) + 1:
			path += (r*pi/2 - 2*r) * length
		else:
			path += (r*pi/2 - 2*r) * (length-1) + (r*pi - 2*r)
print(path)
