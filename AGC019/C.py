from math import pi

input1 = list(map(int,input("").split(" ")))
N = int(input(""))
src = {"x":input1[0],"y":input1[1]}
dist = {"x":input1[2],"y":input1[3]}

spring = []
for i in range(N):
	temp = list(map(int,input("").split(" ")))
	if temp[0] in range(min(src['x'],dist['x']),max(src['x'],dist['x'])+1):
		if temp[1] in range(min(src['y'],dist['y']),max(src['y'],dist['y'])+1):
			spring.append({'x':temp[0], 'y':temp[1], 'distance':(abs(temp[0]-src['x']) + abs(temp[1]-src['y']))})

# print(spring)
path = (abs(src['x']-dist['x']) + abs(src['y']-dist['y'])) * 100
if len(spring) > 0:
	r = 10
	if src['x'] == dist['x'] or src['y'] == dist['y'] :
		#半円
		path += r*pi - 2*r 
	else:
		#1/4円
		spring.sort(key=lambda k: k['distance'])
		via = []
		via.append(spring[0])
		spring.pop(0)
		while len(spring) > 0:
			if spring[0]['x'] in range(min(dist['x'],via[-1]['x']),max(dist['x'],via[-1]['x'])+1):
				if spring[0]['y'] in range(min(dist['y'],via[-1]['y']),max(dist['y'],via[-1]['y'])+1):
					via.append(spring[0])
			spring.pop(0)

		path += (r*pi/2 - 2*r) * len(via)

print(path)