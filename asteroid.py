import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    color = ASTEROID_COLOR if "ASTEROID_COLOR" in globals() else (255, 255, 255)
    pos = (int(self.position.x), int(self.position.y))
    pygame.draw.circle(screen, color, pos, int(self.radius), 2)

  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if(self.radius <= ASTEROID_MIN_RADIUS):
      return
    else:
      newAngle = random.uniform(20, 50)
      newRadius = self.radius - ASTEROID_MIN_RADIUS
      
      a1 = Asteroid(self.position.x, self.position.y, newRadius)
      a2 = Asteroid(self.position.x, self.position.y, newRadius)
      
      v1 = self.velocity.rotate(-newAngle) * 1.2
      v2 = self.velocity.rotate(newAngle) * 1.2
      
      a1.velocity = v1
      a2.velocity = v2
       
      