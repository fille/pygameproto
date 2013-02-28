import os, sys
import pygame
import math
import random
import time
from decimal import Decimal
from pygame.locals import *

MAX_speed = 0.05

class Planet(pygame.sprite.Sprite):
	def __init__(self,initial_position,size,objs,id,color):
		self.id = id
		self.weight = 10.0
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
		pygame.draw.circle(self.image,color,(self.getsizeCircle(),self.getsizeCircle()),self.getsizeCircle(),self.getsizeCircle())
		self.area = screen.get_rect()

	def getsizeRect(self):
		if self.type == 1:
			return [10,10]
		elif self.type == 2 :
			return [45,45]
	
	def getsizeCircle(self):
		if self.type == 1:
			return 10;
		if self.type == 2:
			return 20;
	def getWeight(self):
		if self.type == 1:
			return 100
		if self.type == 2:
			return 10000;
	def update(self):
			 	
		for current in self.plants :	
			
			if current.type != 2:
				 current.rect.center =self.force(current)
		
		
			
			#print current.id + ":" +str(current.rect.center[0])
		
	def force(self,current):
			if self.type == 2:
				r = 0.0;
				distance = 0.0;
				mass = 0.0;
				force = 0.0;
				forceX = 0.0;
				forceY = 0.0;
				coord = 0.0;
				x = current.rect.center[0] 
			  	y = current.rect.center[1] 
		                diffX  = self.rect.center[0] - current.rect.center[0] 
		                diffY  =  self.rect.center[1]-current.rect.center[1]
				distance = ((diffX**2.0 )+ (diffY**2))**0.5
				mass = current.getWeight() * self.getWeight()
				
				r = distance**2
			        if r > 0.0001:
				 force = mass / r
				 speed = MAX_speed *(force)
			  	 rateX =  speed*(diffX/distance) 
			  	 rateY =  speed *(diffY/distance)
			
				 x += rateX+0.4
				 y += rateY+0.4
				if current != self:
					 return (x,y)
						    
				else:
				 return current.rect.center
			else:
				return current.rect.center
			    
 
def main():
 pygame.init()
 screen = pygame.display.set_mode((640, 480))
 background = pygame.Surface(screen.get_size())
 background = background.convert()
 objs = []
 i = 0

 plan4  = Planet([250,200],1,objs,"a",(0,0,200))
 objs.append(plan4)
 #plan2  = Planet([50,200],2,objs,"a",(200,0,0))
 plan3  = Planet([490,200],2,objs,"a",(200,0,0))
 #objs.append(plan2)
 objs.append(plan3)
 for i in range(0,100):	
 	plan1  = Planet([random.randint(0,640),random.randint(0,480)],1,objs,"a",(0,0,200))
 	objs.append(plan1)

 circlesprite =  pygame.sprite.Group(objs);

 clock = pygame.time.Clock()
 while 1 :
  clock.tick(60)
  circlesprite.clear(screen,background);
  circlesprite.update();
  circlesprite.draw(screen)
  pygame.display.flip()

if __name__ == "__main__":
    main()



