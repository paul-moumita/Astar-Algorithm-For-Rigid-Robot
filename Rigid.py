# Author : Moumita Paul
# Project3 Phase2 


import pygame
import numpy as np 
import sys
import os
import math
from time import time
from pygame.locals import *
import Image
from OpenGL.GL import *
from OpenGL.GLU import *




# ----------------------------#
#			  INPUTS		  #
# ----------------------------#




# print("User Defined Inputs")
# radius=float(input(" Enter Robot radius =  "))
# clearance=float(input("Enter clearence =  "))
# print("Enter start point cordinates")
# x_i=float(input("xs =  "))
# y_i=float(input("ys =  "))
# print("Enter goal node cordinates")
# x_g=float(input("xg =  "))
# y_g=float(input("yg =  "))
# resolution=int(input("Enter Resolution (must be an integer value) =  "))
# Theta_s = float(input("Enter Theta_s="))
# d= float(input("Enter step size of movements(must be within 1-10")

radius=1
clearance=1

x_i=50
y_i=30

x_g=150
y_g=150
resolution=1
Theta_s = 60
d= 1


start = [x_i,y_i]
goal = [x_g,y_g]

rows = 200/resolution
coloums = 300/resolution 

start = [m/resolution for m in start]
goal = [n/resolution for n in goal]



# Color 

sky_blue = [135,206,235]
red = [255,0,0]
lime = [0,255,0]
white = [255,255,255]

#-------------------------------------#
#			Defining Functions
#-------------------------------------#



#  To display obstacles 
def obstacles_display(x,y,resolution):
	obs_pix = 0
	# Circle
	if ((x-math.ceil(225/resolution))**2+math.ceil(y-(150/resolution))**2-math.ceil(25/resolution)**2)<=0:
		obs_pix = 1

	# Ellipse
	if ((x-math.ceil(150/resolution))/math.ceil(40/resolution))**2+((y-math.ceil(100/resolution))/math.ceil(20/resolution))**2 - 1<=0:
		obs_pix = 1

	# Tilted Rectangle
	x_pts = np.array([95,95+10*math.cos(math.radians(60)), 95-75*math.cos(math.radians(30))+10*math.cos(math.radians(60)), 95-75*math.cos(math.radians(30))])/resolution
	y_pts = np.array([30,30+10*math.sin(math.radians(60)), 30+75*math.sin(math.radians(30))+10*math.sin(math.radians(60)), 30+75*math.sin(math.radians(30))])/resolution

	l1 = (y-y_pts[0]) >= ((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))*(x-x_pts[0])    
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1])    
	l3 = (y-y_pts[2]) <= ((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))*(x-x_pts[2])    
	l4 = (y-y_pts[3]) >= ((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))*(x-x_pts[3]) 

	if (l1 and l2 and l3 and l4):
		obs_pix = 1

	# Rhombus
	x_pts = np.array([225,254.15,225,195.85])/resolution
	y_pts = np.array([10,25,40,25])/resolution

	l1 = (y-y_pts[0]) >= ((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))*(x-x_pts[0])    
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1])    
	l3 = (y-y_pts[2]) <= ((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))*(x-x_pts[2])    
	l4 = (y-y_pts[3]) >= ((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))*(x-x_pts[3]) 

	if (l1 and l2 and l3 and l4):
		obs_pix = 1

	# Polygon 1
	x_pts = np.array([75,100,75,50])/resolution
	y_pts = np.array([120,150,185,150])/resolution

	l1 = (y-y_pts[0]) >= ((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))*(x-x_pts[0])    
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1])
	l3 = (y-y_pts[2]) <= ((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))*(x-x_pts[2]) 
	l4 = (y-y_pts[3]) >= ((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))*(x-x_pts[3]) 

	if (l1 and l2 and l3 and l4):
		obs_pix = 1

	# Polygon 2 
	x_pts = np.array([75,25,20])/resolution
	y_pts = np.array([185,185,120])/resolution   
	l5 = (y-y_pts[0]) <= 0
	l6 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1]) 
	l7 = (y-y_pts[2]) >= ((y_pts[0]-y_pts[2])/(x_pts[0]-x_pts[2]))*(x-x_pts[2])
	
	if (l5 and l6 and l7):
		obs_pix = 1

	return obs_pix

	

# Creating Map with obstacles
def Map(x,y,resolution,d=radius+clearance):
	q=0
	if (x<(d/resolution)) or (x>(300-d)/resolution) or (y<(d/resolution)) or (y>(200-d)/resolution):
		q=1
	if ((x-math.ceil(225/resolution))**2+(y-math.ceil(150/resolution))**2-(math.ceil((25+d)/resolution))**2)<0:
		q=1
	if ((x-math.ceil(150/resolution))/(math.ceil(40+d)/resolution))**2 + ((y - math.ceil(100/resolution))/(math.ceil(20+d)/resolution))**2 - 1 < 0:
		q=1
	
	x_pts = np.array([95,95+10*math.cos(math.radians(60)), 95-75*math.cos(math.radians(30))+10*math.cos(math.radians(60)), 95-75*math.cos(math.radians(30))])/resolution
	y_pts = np.array([30,30+10*math.sin(math.radians(60)), 30+75*math.sin(math.radians(30))+10*math.sin(math.radians(60)), 30+75*math.sin(math.radians(30))])/resolution

	l1 = (y-y_pts[0]) >= ((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))*(x-x_pts[0]) - d/resolution*(1+math.sqrt(((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))**2))    
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1]) + d/resolution*(1+math.sqrt(((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))**2))  
	l3 = (y-y_pts[2]) <= ((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))*(x-x_pts[2]) + d/resolution*(1+math.sqrt(((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))**2))    
	l4 = (y-y_pts[3]) >= ((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))*(x-x_pts[3]) - d/resolution*(1+math.sqrt(((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))**2)) 

	if (l1 and l2 and l3 and l4):
		q = 1

	# Rhombus
	x_pts = np.array([225,250,225,200])/resolution
	y_pts = np.array([10,25,40,25])/resolution

	l1 = (y-y_pts[0]) >= ((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))*(x-x_pts[0]) - d/resolution*(1+math.sqrt(((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))**2))    
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1]) + d/resolution*(1+math.sqrt(((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))**2))  
	l3 = (y-y_pts[2]) <= ((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))*(x-x_pts[2]) + d/resolution*(1+math.sqrt(((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))**2))    
	l4 = (y-y_pts[3]) >= ((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))*(x-x_pts[3]) - d/resolution*(1+math.sqrt(((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))**2))

	if (l1 and l2 and l3 and l4):
		q = 1
	# Polygon 1
	x_pts = np.array([75,100,75,50])/resolution
	y_pts = np.array([120,150,185,150])/resolution

	l1 = (y-y_pts[0]) >= ((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))*(x-x_pts[0]) - d/resolution*(1+math.sqrt(((y_pts[1]-y_pts[0])/(x_pts[1]-x_pts[0]))**2))    
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1]) + d/resolution*(1+math.sqrt(((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))**2))  
	l3 = (y-y_pts[2]) <= ((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))*(x-x_pts[2]) + d/resolution*(1+math.sqrt(((y_pts[3]-y_pts[2])/(x_pts[3]-x_pts[2]))**2))    
	l4 = (y-y_pts[3]) >= ((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))*(x-x_pts[3]) - d/resolution*(1+math.sqrt(((y_pts[0]-y_pts[3])/(x_pts[0]-x_pts[3]))**2))
	if (l1 and l2 and l3 and l4):
		q = 1

	# Polygon 2 
	x_pts = np.array([75,25,20])/resolution
	y_pts = np.array([185,185,120])/resolution   
	l1 = (y-y_pts[0]) <= 0 + d/resolution
	l2 = (y-y_pts[1]) <= ((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))*(x-x_pts[1]) - d/resolution*(1+math.sqrt(((y_pts[2]-y_pts[1])/(x_pts[2]-x_pts[1]))**2))
	l3 = (y-y_pts[2]) >= ((y_pts[0]-y_pts[2])/(x_pts[0]-x_pts[2]))*(x-x_pts[2]) - d/resolution*(1+math.sqrt(((y_pts[0]-y_pts[2])/(x_pts[0]-x_pts[2]))**2))
	

	if (l1 and l2 and l3):
		q = 1

	return q

# Heuristic
def heuristic(node):
	h = math.sqrt ( (node[0] - goal[0])**2 +  (node[1] - goal[1])**2 )
	return h

# ---------Defining 8 possible moves of robot-----#

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
#-------------------------------------------#
#-------------------------------------------#


#----------Exploration of the Robot---------#
point_node = [start]
c_nd = [start]
heuristic_node = [round(heuristic(start),2)]
vp_nd=[]
vc_nd=[]
v_cst=[]
vh_nd=[]

# Workspace  defined
if (Map(goal[0],goal[1],resolution)== 1 or Map(start[0],start[1],resolution)):
	sys.exit(" Error: goal point or start point lies within the obstacles")
if(start[0] not in range (0,301) or goal[0] not in range (0,301) or start[1] not in range(0,201) or goal[1] not in range(0,201)):
	sys.exit("Error: Entered point outside the workspace")


x=0 
cst = [0]
ndx = start
flag = 0
exit = 0 
count =0
start_time = time()
while(flag!=1 and c_nd !=[]):
	
	# To move up
	nd, cost = up_move(ndx)
	if(nd[1]>=0 and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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

	
	# To move down
	nd, cost = down_move(ndx)
	if(nd[1]<=rows and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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


	
	# To move right
	nd, cost = right_move(ndx)
	if(nd[0]<= coloums and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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


	# To move left
	nd, cost = left_move(ndx)
	if(nd[0]>=0 and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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


	# To move down_left
	nd, cost = down_left_move(ndx)
	if(nd[1]<=rows and nd[0]>=0 and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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


	# To move down_right
	nd, cost = down_right_move(ndx)
	if(nd[1]<=rows and nd[0]<=coloums and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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


	# To move up_left
	nd, cost = up_left_move(ndx)
	if(nd[1]>=0 and nd[0]>=0 and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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


	# To move up_right
	nd, cost = up_right_move(ndx)
	if(nd[0]<=coloums and nd[1]>=0 and Map(nd[0],nd[1],resolution)!=1):
		if nd not in vc_nd:
			xl=range(0,len(c_nd))
			xl = xl[::-1]
			check = 0
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
	
	vp_nd.append(point_node.pop(x))
	vc_nd.append(c_nd.pop(x))
	v_cst.append(cst.pop(x))
	vh_nd.append(heuristic_node.pop(x))

	if (vc_nd[-1]== goal):
		flag=1
	if (flag!=1 and c_nd!=[]):
		x = heuristic_node.index(min(heuristic_node))
		ndx = c_nd[x][:]

# To check the desired path
if(flag == 0 and c_nd ==[]):
	sys.exit("Path not available")

sequence=[]
sequence.append(vc_nd[-1])
sequence.append(vp_nd[-1])
x = vp_nd[-1]
i = 1
while(x!=start):
	if (vc_nd[-i]==x):
		sequence.append(vp_nd[-i])
		x  = vp_nd[-i]
	i = i+1

# Creating obstacles spaces 
obstacles_spaces = []
for i in range (0,301):
	for j in range (0,201):
		q = obstacles_display(i,j,resolution)
		if q == 1:
			obstacles_spaces.append([i,j])

k=5
my_list = np.array(vc_nd)
vc_nd = my_list*k*resolution
my_list_1 = np.array(sequence)
sequence = my_list_1*k*resolution
my_list_2 = np.array(obstacles_spaces)
obstacles_spaces = my_list_2*k*resolution	

pygame.init()

#----------------------------------------#
#----------------------------------------#

#-------------Displaying Output----------#


# Size of the screen
size = [300*k+resolution+resolution,200*k+resolution+resolution]
screen = pygame.display.set_mode(size)
# save_screen = make_video(screen)
# video = False

# Display Window
pygame.display.set_caption("Output")
clock = pygame.time.Clock()
done = False
end_time = time()

# To calculate the solving time for the algorithm 
print("Time taken {} seconds to solve".format(end_time-start_time))

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		

	screen.fill(sky_blue)

	# To display obstacles
	for i in obstacles_spaces:
		pygame.event.get()
		pygame.draw.rect(screen,lime,[i[0],200*k-i[1],resolution*k,resolution*k])
	
	pygame.display.flip()
	clock.tick(200)
	
	# To display explored nodes
	for i in vc_nd:
		pygame.event.get()
		pygame.time.wait(1)
		pygame.draw.rect(screen,white,[i[0],200*k-i[1],resolution*k,resolution*k])
		
		pygame.display.flip()

	# To display Optimal path
	for j in sequence[::-1]:
		pygame.time.wait(1)
		pygame.draw.rect(screen,red,[j[0],200*k-j[1],resolution*k,resolution*k])
		pygame.display.flip()
	
	pygame.display.flip()
	pygame.time.wait(10)
	done = True
	
	# pygame.display.update()
	# pygame.time.delay(2000)

	

	# buf = glReadPixels(0,0,300,200,GL_RGB,GL_BYTE)
	# img= Image.frombuffer('RGB',300,200,buf)
	# img2 = ImageOps.flip(img)
	# img2.save('frame%061.png'%(farme_number))
	
	
	# if video: 
	# 	next(save_screen)
	# 	print("IN main")

	pygame.quit()
