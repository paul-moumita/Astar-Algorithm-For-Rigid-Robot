import pygame
import numpy as np 
import sys
import math
from PLI import Image


start_node = [x_i,y_i]
goal node = [x_g,y_g]

rows = 200/resolution
coloums = 300/resolution 

start = [m/resolution for m in start]
goal = [n/resolution for n in goal]

point_node = [start]
cost_node = [start]
heuristic_node = [round(heuristic(start),2)]
vp_nd=[]
vc_nd=[]
v_cst=[]
vh_nd=[]

x=0 
cost = [0]
ndx = start
flag = 0
exit = 0 
count =0

obstacles_space = []
for i in range (0,301):
	for j in range (0,201):
		q = obstacles_display(i,j,resolution)
		if q = 1:
			obstacles_space.append([i,j])

k=2
my_list = np.array(vc_nd)
vc_nd = my_list*k*resolution
my_list_1 = np.array(sequence)
sequence = my_list_1*k*resolution
my_list_2 = np.array(obstacles_space)
obstacles_space = my_list_2*k*resolution


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