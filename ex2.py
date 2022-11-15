import math
def dif(x,y):
	return (pow(x,2)+pow(y,2))

def RK(x,y,h):
	k1 = h*dif(x,y)
	k2 = h*dif(x+h/2,y+k1/2)
	k3 = h*dif(x+h/2,y+k2/2)
	k4 = h*dif(x+h,y+k3)
	k = 1/6*(k1+2*k2+2*k3+k4)

	return k
def main():
	h = 0.01
	xf= 0.8
	x0 = 0
	y0 = 1
	while x0<=xf:
		y0 = y0 + RK(x0,y0,h)
		x0 += h
	print(y0)
main()