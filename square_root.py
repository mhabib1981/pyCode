import math

inputFile=open('square_root_input.txt','r').readlines()


def read_input():
	for line in inputFile:
		x=line.strip('\n')
		x=x.split(" ")
		sqrt_approx(x[0], x[1])

def sqrt_approx(value,steps):
	r=1
	d=float(value)/r
	print d

read_input()
