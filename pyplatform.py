import os, sys
import pygame
import math
import time
from decimal import Decimal
from pygame.locals import *

class Wall(pygame.sprite.Sprite):
	
	def __init__(self,initial_position,width):
		pygame.sprite.Sprite.__init__(self)
		self.screen = pygame.display.get_surface();
		self.image = pygame.Surface((width,20))
		self.rect = self.image.get_rect();
		self.rect.topleft = initial_position;
		self.image.fill((255,0,0));


class Gubbe(pygame.sprite.Sprite):

	
	def __init__(self,initial_position,walls):
		pygame.sprite.Sprite.__init__(self)
		self.screen = pygame.display.get_surface();
		self.image = pygame.Surface((20,20))
		self.rect = self.image.get_rect();
		self.rect.topleft = initial_position;
		self.image.fill((0,10,200));
		self.max_jump = 10;
		self.jumpacc = 0.0;
		self.jumpMe = 0
		self.max_walk = 10;
		self.walk_acc = 0.0
		self.run = 0
		self.dir = 0
		self.walls = walls
		self.typehit = 0
			
	def jump(self):
		if self.jumpMe  != 1 :
			self.jumpacc = 1.0;
  			self.jumpMe = 1;
	def walk(self,dir):
		self.run = 1
		self.dir = dir
		if self.walk_acc < 1 :
			self.walk_acc += 0.1
	def collide(self):
		for wall in self.walls:
			if self.rect.topleft[1] < wall.rect.bottomleft[1] and self.rect.topleft[0] < wall.rect.bottomright[0]:
				if self.jumpMe  != 1 :				
					self.typehit = 1
					self.jumpacc = -0.8
			if self.rect.bottomleft[1] > wall.rect.topleft[1] and self.rect.bottomright[0] < wall.rect.topright[0]:
				if self.jumpMe  != 1 :				
					self.jumpacc = 0
				
				
		  		
		
	def update(self):
		
		self.collide()
		moveX = self.rect.center[0];
		moveY = self.rect.center[1];
		newdis = 0; 
		if self.jumpMe == 1:
				print self.jumpacc
				if self.jumpacc > 0.0 :
					newdis= self.jumpacc * self.max_jump;
					
					self.jumpacc -= 0.1
				if self.jumpacc < 0.0:
					self.jumpMe  = 0
					
						
		
		else:
			newdis= self.jumpacc * self.max_jump;
			self.jumpacc -= 0.1
		
			 
		newX = self.walk_acc * self.max_walk
	
		moveY = self.rect.center[1] - newdis;
		if self.dir == 2:
			moveX = self.rect.center[0] -newX;
		elif self.dir == 1: 
			moveX = self.rect.center[0] +newX;
		
		if self.run == 0 :		
			if self.walk_acc > 0.1 :		
				self.walk_acc -= 0.1
			if self.walk_acc < -0.1 :
				print self.walk_acc 		
				self.walk_acc += 0.1	
		self.rect.center = (moveX,moveY)
		self.run = 0;
		self.typehit = 0;


def main():
 pygame.init()
 screen = pygame.display.set_mode((640, 480))
 background = pygame.Surface(screen.get_size())
 background = background.convert()

 walla = Wall((10,380),400)
 obj = Gubbe((100,300),[walla])
 sprites =  pygame.sprite.Group((obj,walla))
 running = True
 while(running):
  time.sleep(0.1)
  sprites.clear(screen,background);
  sprites.update();
  sprites.draw(screen)
  pygame.display.flip()
 
  for event in pygame.event.get():
	
	if event.type == pygame.QUIT:
		running = False

  key=pygame.key.get_pressed() 
  if key[K_SPACE] :
	obj.jump();
  elif key[K_RIGHT] :
	obj.walk(1);
  elif key[K_LEFT] :
	obj.walk(2);
if __name__ == "__main__":
    main()

