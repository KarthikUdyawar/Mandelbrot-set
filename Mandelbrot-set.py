# Import
import pygame
import colorsys
import math

# initialization
xoff =  0.2501   
yoff = 0       
iteration = 0 
scale = 2
backgroundSize = [300,300]
MID = [backgroundSize[0]/2,backgroundSize[1]/2]

def map(value,changed,og):
	return (value-changed[0])*(float(og[1]-og[0])/float(changed[1]-changed[0]))+og[0]

def mandlebrot(X,Y,og=False):
	x = map(X,[0,backgroundSize[0]],[-scale,scale])
	y = map(Y,[0,backgroundSize[1]],[-scale,scale])
	if not og:
		z = complex(x+xoff,y+yoff)
		c=z
		if (z.real+1)**2+z.imag**2>1/16:
			try:
				for i in range(iteration):
					if z.real*z.real+z.imag*z.imag>4:
						return ((math.sin(i*0.0001)+1)/2)*255
					z = z**2+c		# Formula
			except:
				return ((math.sin(i*0.0001)+1)/2)*255
		return None

# Main loop
if __name__=='__main__':
	pygame.init()
	screen = pygame.display.set_mode(backgroundSize)
	pygame.display.set_caption("Mandlebrot Set")
	print("Point of zoom: ",(xoff,yoff))
	running = True
	while running:
		print ("Iteration: ",iteration,"\tScale: ",scale)
		for x in range(backgroundSize[0]):
			for y in range(backgroundSize[1]):
				for event in pygame.event.get(): 
					if event.type == pygame.QUIT:
						running = False

				temp = mandlebrot(x,y)
				if temp:
					v,h = 255, temp
				else:
					v,h = 0,0
				screen.set_at((x,y),colorsys.hsv_to_rgb(h,1,v))

		pygame.display.flip()
		scale*=0.5				
		iteration+=20
		