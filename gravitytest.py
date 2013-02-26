import os, sys
import pygame
import math
import time
from decimal import Decimal
from pygame.locals import *

MAX_speed = 3

class Planet(pygame.sprite.Sprite):
	def __init__(self,initial_position,size,objs,id):
		self.id = id
		self.weight = 10
		self.type = size
		self.x = initial_position[0]
		self.y = initial_position[1]
		self.plants = objs
		pygame.sprite.Sprite.__init__(self)
		screen = pygame.display.get_surface();
		self.image = pygame.Surface(self.getsizeRect())
		self.rect = self.image.get_rect();
		self.rect.topleft = initial_position;
		self.image.fill((40,0,0));
		pygame.draw.circle(self.image,(255,0,0),(self.getsizeCircle(),self.getsizeCircle()),self.getsizeCircle(),self.getsizeCircle())
		self.area = screen.get_rect()

	def getsizeRect(self):
		if self.type == 1:
			return [22,22]
		elif self.type == 2 :
			return [45,45]
	
	def getsizeCircle(self):
		if self.type == 1:
			return 10;
		if self.type == 2:
			return 20;
	def getWeight(self):
		if self.type == 1:
			return 0.01
		if self.type == 2:
			return 0.1;
	def update(self):
		for current in self.plants : 	
			 current.rect.center =self.force(current)    
			
			
			#print current.id + ":" +str(current.rect.center[0])
		
	def force(self,current):
				r = 0;
				distance = 0;
				mass = 0;
				force = 0;
				forceX = 0;
				forceY = 0;
				coord = 0;
				x = current.rect.center[0] 
			  	y = current.rect.center[1] 
		                diffX  = self.rect.center[0] - current.rect.center[0] 
		                diffY  =  self.rect.center[1]-current.rect.center[1]
				distance = ((diffX**2 )+ (diffY**2))**0.5
				mass = current.getWeight() * self.getWeight()
				
				r = distance**2
			        if r != 0:
				 force = mass / r
				 speed = MAX_speed *(force)
			  	 rateX =  speed*(diffX/distance)
			  	 rateY =  speed *(diffY/distance)
				 print str(rateX)
				 x += rateX		
				 y += rateY	
				if current.id != self.id:
				 print current.id  + "-" + self.id
				 return (x,y)
				else:
				 return current.rect.center
						    
  
 
def main():
 pygame.init()
 screen = pygame.display.set_mode((640, 480))
 background = pygame.Surface(screen.get_size())
 background = background.convert()
 objs = []
 plan1  = Planet([300,200],1,objs,"a")
 plan2  = Planet([200,40],1,objs,"b")
 plan3  = Planet([300,300],1,objs,"c")
 plan4  = Planet([300,300],1,objs,"d")
 plan5  = Planet([500,300],1,objs,"e")
 plan6  = Planet([320,220],2,objs,"f")
 plan7  = Planet([30,400],1,objs,"g")
 objs.append(plan1)
 objs.append(plan2)
 objs.append(plan3)
 objs.append(plan4)
 objs.append(plan5)

 objs.append(plan7)
 objs.append(plan6)
 circlesprite =  pygame.sprite.Group((plan1,plan2,plan3,plan4,plan5,plan6,plan7));

 clock = pygame.time.Clock()
 while 1 :
  clock.tick(20)
  circlesprite.clear(screen,background);
  circlesprite.update();
  circlesprite.draw(screen)
  pygame.display.flip()

if __name__ == "__main__":
    main()



