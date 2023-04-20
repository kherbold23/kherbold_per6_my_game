import pygame as pg

from pygame.sprite import Sprite

from settings import *

from random import randint

vec = pg.math.Vector2
# player class

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(22,0)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.standing = False
    def input(self):
        keystate = pg.key.get_pressed()
        
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
    
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
     
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        # if hits:
        self.vel.y = -PLAYER_JUMP
    
    def inbounds(self):
        if self.rect.x > WIDTH - 50:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            self.pos.y = HEIGHT - 25
            self.vel.y = 0
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            self.pos.y = HEIGHT - 575
            self.vel.y = 0
            print("i am off the top of the screen...")

    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                self.game.score += 1
                print(SCORE)
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    
class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 700)
        self.pos = vec(400, HEIGHT/2)
        self.vel = vec(randint(1,4),randint(1,3))
        self.acc = vec(1,1)
        self.cofric = 0.24
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
        if self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y < 0:
            self.vel.y *= -1
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            
    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos

# create a new platform class...

class Platform(Sprite):
    def __init__(self, x,y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant

class Ufo(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.image = pg.Surface([100, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 580
        self.speed = 5
    def update(self):
        if self.rect.x > self.width:
            self.rect.x = self.width
        elif self.rect.x < 0:
            self.rect.x = 0