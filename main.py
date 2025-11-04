import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameclock = pygame.time.Clock()
    dt = 0

    # sprite group declaration
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

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
        
        
         # Debug prints
        print(f"Total sprites: {len(drawable)}")
        print(f"Total asteroids: {len(asteroids)}")
        
        print("Drawable contents:")
        for s in list(drawable)[:10]:
            print(type(s).__name__, int(s.position.x), int(s.position.y), getattr(s, "radius", None))
        
        #draw gameobjects individually
        for sprite in drawable:
            sprite.draw(screen)
            # Debug: Draw red dot at sprite position
            pos = (int(sprite.position.x), int(sprite.position.y))
            pygame.draw.circle(screen, (255, 0, 0), pos, 3)
            
        pygame.display.flip()
        dt = (gameclock.tick(60)/1000)
        #print(f"secconds: {dt}")

if __name__ == "__main__":
    main()
    
