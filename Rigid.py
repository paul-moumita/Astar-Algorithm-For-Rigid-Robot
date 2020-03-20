# Author : Moumita Paul
# Project3 Phase2 



import pygame
import numpy as np 
import sys
import math
from PLI import Image


# ----------------------------#
#			  INPUTS		  #
# ----------------------------#


start = [x_i,y_i]
goal = [x_g,y_g]

print("Enter robot parameters")
radius=float(input("radius =  "))
clearance=float(input("clearence =  "))
print("Enter initial node cordinates")
x_i=float(input("x =  "))
y_i=float(input("y =  "))
print("Enter goal node cordinates")
x_g=float(input("x =  "))
y_g=float(input("y =  "))
resolution=int(input("Enter Resolution (must be an integer value) =  "))



rows = 200/resolution
coloums = 300/resolution 

start = [m/resolution for m in start]
goal = [n/resolution for n in goal]

point_node = [start]
c_nd = [start]
heuristic_node = [round(heuristic(start),2)]
vp_nd=[]
vc_nd=[]
v_cst=[]
vh_nd=[]

x=0 
cst = [0]
ndx = start
flag = 0
exit = 0 
count =0

obstacles_spaces = []
for i in range (0,301):
	for j in range (0,201):
		q = obstacles_display(i,j,resolution)
		if q = 1:
			obstacles_spaces.append([i,j])

k=2
my_list = np.array(vc_nd)
vc_nd = my_list*k*resolution
my_list_1 = np.array(sequence)
sequence = my_list_1*k*resolution
my_list_2 = np.array(obstacles_spaces)
obstacles_spaces = my_list_2*k*resolution


# Color

black = [0,0,0]
red = [255,0,0]
blue = [0,100,255]
white = [255,255,255]

# Size of the screen
size = [300*k+resolution+resolution,200*k+resolution+resolution]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Output")
clock = pygame.time.Clock()
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			screen.fills(black)


def obstacles_display(x,y,resolution):
	clearance = 0
	if ((x-math.ceil(225/resolution))**2+math.ceil(y-(150/resolution))**2-math.ceil(25/resolution)**2)<=0:
        c=1
    if ((x-math.ceil(150/resolution))/math.ceil(40/resolution))**2 + ((y - math.ceil(100/resolution))/math.ceil(20/resolution))**2 - 1 <=0:
        c=1
    return c

def Map(x,y,resolution,d=radius+clearance):
	q=0
	if ((x-math.ceil(225/resolution))**2+(y-math.ceil(150/resolution))**2-(math.ceil((25+d)/resolution))**2)<0:
        q=1
    if ((x-math.ceil(150/resolution))/(math.ceil(40+d)/resolution))**2 + ((y - math.ceil(100/resolution))/(math.ceil(20+d)/resolution))**2 - 1 < 0:
        q=1
    return q


def heuristic(node):
	h = math.sqrt ( (node[0] - goal[0])**2 +  (node[1] - goal[1])**2 )
    return h

# Defining 8 possible moves of robot

def left_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]-1
	node_xy[1] = nodes[1]
	cost = 1
	return node_xy,cost


def right_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]+1
	node_xy[1] = nodes[1]
	cost = 1
	return node_xy,cost


def up_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]
	node_xy[1] = nodes[1]-1
	cost = 1
	return node_xy,cost


def down_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]
	node_xy[1] = nodes[1]+1
	cost = 1
	return node_xy,cost


def down_left_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]-1
	node_xy[1] = nodes[1]+1
	cost = 1.42
	return node_xy,cost


def down_right_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]+1
	node_xy[1] = nodes[1]+1
	cost = 1.42
	return node_xy,cost


def up_left_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]-1
	node_xy[1] = nodes[1]-1
	cost = 1.42
	return node_xy,cost


def up_right_move(nodes):
	node_xy = [0,0]
	node_xy[0] = nodes[0]+1
	node_xy[1] = nodes[1]-1
	cost = 1.42
	return node_xy,cost


if (obstacles_space(goal[0],goal[1,resolution])== 1 or obstacles_space(start[0],start[1],resolution)):
	sys.exit(" Error")
if(start[0] not in range (0,301) or goal[0] not in range (0,301) or start[1] not in range(0,201) or goal[1] not in range(0,201)):
	sys.exit("Error Outside")



while(flag!=1 and c_nd !=[]):
	# To move Right
	nd, cost = up(ndx)
	if(nd[1]>=0 and obstacles_space(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check 0
			for p in xl:
				if (nd == c_nd[p]):
					check= 1
					if (cst[p]>=(cst[x]+cost)):
						point_node[p]=ndx
						cst[p]=round((cst[x]+cost),1)
						break
			if(check!=1):
				point_node.append(ndx)
				c_nd.append(nd)
				cst.append(round(cost+cst[x],1))
				heuristic_node.append(round((cost+cst[x]+heuristic(nd)),2))

	nd, cost = down(ndx)
	if(nd[1]<=rows and obstacles_space(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check 0
			for p in xl:
				if (nd == c_nd[p]):
					check= 1
					if (cst[p]>=(cst[x]+cost)):
						point_node[p]=ndx
						cst[p]=round((cst[x]+cost),1)
						break
			if(check!=1):
				point_node.append(ndx)
				c_nd.append(nd)
				cst.append(round(cost+cst[x],1))
				heuristic_node.append(round((cost+cst[x]+heuristic(nd)),2))


	nd, cost = right(ndx)
	if(nd[0]<= coloums and obstacles_space(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check 0
			for p in xl:
				if (nd == c_nd[p]):
					check= 1
					if (cst[p]>=(cst[x]+cost)):
						point_node[p]=ndx
						cst[p]=round((cst[x]+cost),1)
						break
			if(check!=1):
				point_node.append(ndx)
				c_nd.append(nd)
				cst.append(round(cost+cst[x],1))
				heuristic_node.append(round((cost+cst[x]+heuristic(nd)),2))

	nd, cost = left(ndx)
	if(nd[0]>=0 and obstacles_space(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check 0
			for p in xl:
				if (nd == c_nd[p]):
					check= 1
					if (cst[p]>=(cst[x]+cost)):
						point_node[p]=ndx
						cst[p]=round((cst[x]+cost),1)
						break
			if(check!=1):
				point_node.append(ndx)
				c_nd.append(nd)
				cst.append(round(cost+cst[x],1))
				heuristic_node.append(round((cost+cst[x]+heuristic(nd)),2))


	