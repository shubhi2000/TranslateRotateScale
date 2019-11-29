# Name- Shubhi Singhal
# Roll No.- 2018195
# Section - A
# Group - 3

fig=input()
import matplotlib.pyplot as p
from matplotlib.patches import Ellipse
from math import cos
from math import sin
import math

angle=0

def polygon(x,y):													# takes x and y as arguments where x and y are lists of x and y coordinates 
	p.plot(x,y)														# of the vertices, respectively and plots the polygon.
	p.plot([x[0],x[-1]],[y[0],y[-1]])
	p.pause(4)

	
def disc(a,b,rx,ry,angle=0):										# (a,b) is centre of ellipse, rx and ry are semi-minor and semi-major axes 
	x=p.gca()														# this function plots the disc(ellipse)
	e=Ellipse((a,b),2*rx,2*ry,angle,color='b')
	x.add_patch(e)
	x.set_xlim(a-rx-5,a+rx+5)
	x.set_ylim(b-ry-5,b+ry+5)
	p.pause(4)	

if fig=="disc":
	a,b,r=map(int,input().split())
	rx=r
	ry=r
	disc(a,b,r,r)


elif fig=="polygon":
	x=list(map(int,input().split()))
	y=list(map(int,input().split()))
	polygon(x,y)

i=input()

while(i!="quit"):
	l=list(i.split())
	if len(l)==2:
		l[1]=int(l[1])
	else:
		l[1]=int(l[1])
		l[2]=int(l[2])
	if l[0]=="S":
		l1=[[l[1],0,0],[0,l[2],0],[0,0,1]]
	elif l[0]=="R":
		l1=[[cos(l[1]*math.pi/180),(-1)*sin(l[1]*math.pi/180),0],[sin(l[1]*math.pi/180),cos(l[1]*math.pi/180),0],[0,0,1]]
	elif l[0]=="T":
		l1=[[1,0,l[1]],[0,1,l[2]],[0,0,1]]
	if fig=="polygon":
		l3=[]
		l4=[]
		for n in range(len(x)):
			l2=[]
			for m in range(2):
				l2.append(l1[m][0]*x[n]+l1[m][1]*y[n]+l1[m][2]*1)
			l3.append(round(l2[0]))
			l4.append(round(l2[1]))
		x=l3
		y=l4
		
		for n in range(len(x)):
			if n<len(x)-1:
				print(x[n],end=" ")
			else:
				print(x[n])
		for n in range(len(y)):
			if n<len(y)-1:
				print(y[n],end=" ")
			else:
				print(y[n])
		polygon(x,y)

	elif fig=="disc":				
		a1=l1[0][0]*a+l1[0][1]*b+l1[0][2]
		b1=l1[1][0]*a+l1[1][1]*b+l1[1][2]
		if l[0]=="T" or l[0]=="S":
			r1=l1[0][0]*(rx+a)+l1[0][1]*0+l1[0][2]
			r2=l1[1][0]*(0)+l1[1][1]*(ry+b)+l1[1][2]
			a=a1
			b=b1
			rx=r1-a
			ry=r2-b	

		if l[0]=="R":
			a=a1
			b=b1
			angle+=l[1]
		print(str(a)+" "+ str(b)+" "+str(rx)+" "+str(ry))
		disc(a,b,rx,ry,angle)
	i=input()