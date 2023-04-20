# File created by: Kyle Herbold
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries


'''
Game structure:
GOALS; RULES; FEEDBACK; FREEDOM
My goal is:

to create moving platforms for the player to jump on 






'''

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class 

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.water = pg.sprite.Group()
        self.player = Player(self)
        
        
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (39,64,96), "normal")
        self.plat2 = Platform(WIDTH, 500, 0, HEIGHT-50, (39,64,96), "normal")
        # Creating the bottom platform
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.platforms.add(self.plat2)
        self.all_sprites.add(self.player)
        
        # Creates the platforms 
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # Creates Mobs
        for i in range(0,15):
            m = Mob(20,20,(0,200,255))
            self.all_sprites.add(m)
            self.water.add(m)
    # Draw and Update
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # Allow jump via spacebar
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    # Update to add score
    def update(self):
        self.all_sprites.update()
        
        whits = pg.sprite.spritecollide(self.player, self.water, False)
        
        if whits:
            self.score += 1
        #type of platform the block hits and properties
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
# Draw background
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
        self.draw_text(str(self.score), 24, WHITE, 400, 5)
        pg.display.flip()
# Draw text
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
pg.font.init()
font = pg.font.Font(None, 100)
def display_countdown(current_time):
    remaining_time = 10 - int(current_time / 1000)
    if remaining_time < 0:
        remaining_time = 0
    text = font.render(str(remaining_time), True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    self.screen.blit(text, text_rect)

# Set the clock and start time
clock = pg.time.Clock()
start_time = pg.time.get_ticks()

# Start the game loop

while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Calculate the current time and display the countdown
    current_time = pg.time.get_ticks() - start_time
    display_countdown(current_time)

    # Update the screen and control the frame rate
    pg.display.flip()
    clock.tick(60)

    # Quit if the countdown is finished
    if current_time >= 10000:
        running = False


g = Game()

# game loop
while g.running:
    g.new()

pg.quit()