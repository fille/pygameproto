import os, sys
import pygame
import math
import time
from decimal import Decimal
from pygame.locals import *



class Gubbe(pygame.sprite.Sprite):

	
	def __init__(self,initial_position):
		pygame.sprite.Sprite.__init__(self)
		self.screen = pygame.display.get_surface();
		self.image = pygame.Surface((20,20))
		self.rect = self.image.get_rect();
		self.rect.topleft = initial_position;
		self.image.fill((0,50,200));
		self.max_jump = 10;
		self.jumpacc = 0.0;
		self.jumpMe = 0
		self.max_walk = 10;
		self.walk_acc = 0.0
		self.run = 0
		self.dir = 0
			
	def jump(self):
		if self.jumpMe  != 1 :
			self.jumpacc = 1.0;
  			self.jumpMe = 1;
	def walk(self,dir):
		self.run = 1
		self.dir = dir
		if self.walk_acc < 100 :
			self.walk_acc += 10
			   	
		
	def update(self):
		moveX = 0;
		moveY = 0;
		if self.jumpMe == 1:
	  		if self.jumpacc > 0 :
				newdis= self.jumpacc * self.max_jump;
				moveY += newdis
				self.jumpacc -= 0.1
				if self.jumpacc == 0:
					self.jumpacc -=0.1
				  
		        elif self.jumpacc < 0:
				newdis= self.jumpacc * self.max_jump;
				moveY += newdis
				self.jumpacc -= 0.1
				if int(self.jumpacc) == -1.0:
					self.jumpacc = 0
					self.jumpMe = 0
		
				 
		newX = (self.walk_acc*0.01) * self.max_walk
	
		moveY = self.rect.center[1] - moveY;
		if self.dir == 2:
			moveX = self.rect.center[0] -newX;
		elif self.dir == 1: 
			moveX = self.rect.center[0] +newX;
		self.rect.center = (moveX,moveY)
		if self.run == 0 :		
			if self.walk_acc > 0 :
				print self.walk_acc 		
				self.walk_acc -= 10
			if self.walk_acc < 0 :
				print self.walk_acc 		
				self.walk_acc += 10
		
		self.run = 0;


def main():
 pygame.init()
 screen = pygame.display.set_mode((640, 480))
 background = pygame.Surface(screen.get_size())
 background = background.convert()
 obj = Gubbe((100,400))
 sprites =  pygame.sprite.Group((obj))
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

