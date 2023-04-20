WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_JUMP = 20
PLAYER_FRICTION = -0.5
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.5
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255, 255, 0)
GREEN = (0,255,0)
FPS = 60
RUNNING = True 
SCORE = 1
PAUSED = False



PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (175, 100, 50, 20, (200,200,200), "normal")]

UFO = (175,100,50,20, (200,200,200), "ufo")