nodes = '12345678'
x = 'x'
M = [[x,1,2,x,x,x,x,x],\
	 [x,x,1,5,2,x,x,x],\
	 [x,x,x,2,1,4,x,x],\
	 [x,x,x,x,3,6,8,x],\
	 [x,x,x,x,x,3,7,x],\
	 [x,x,x,x,x,x,5,2],\
	 [x,x,x,x,x,x,x,6],\
	 [x,x,x,x,x,x,x,x]]

menor = [[0,0,0]]*len(M)
dists = [0]*len(M)
for j in range(1,len(M)):
	pos = []
	for i in range(0,len(M)):
		if M[i][j] != x:
			dis = dists[i] + M[i][j]
			pos.append([dis,nodes[i],nodes[j]])
	menor[j] = min(pos)
	dists[j] = menor[j][0]

line = menor[-1]
s = '8'
let = '8'
while let != '1':
	p = line[1]
	for q in menor:
		if q[2] == p:
			s = q[2]+'-'+s
			line = q
	let = line[1]
s = '1-'+s

print("Nodos de la ruta mas corta:",s)
print("Distancia:", menor[-1][0])
