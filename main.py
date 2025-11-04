import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameclock = pygame.time.Clock()
    dt = 0

    # sprite group declaration
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #create infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        #update gameobjects
        updatable.update(dt)
        #draw gameobjects individually
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = (gameclock.tick(60)/1000)
        #print(f"secconds: {dt}")

if __name__ == "__main__":
    main()
    
