import math
a = float(input("a? "))
b = float(input("b? "))

h = (b-a)/3


def primera (x):
	return (math.sqrt(4-pow(x,2)))



simp = (3/8)*h*(primera(a) + 3*primera((2*a+b)/3) + 3*primera((a+2*b)/3) + primera(b))

print(simp)
