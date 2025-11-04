import pygame
from circleshape import *
from constants import *

class Shoot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    color = SHOT_COLOR if "SHOT_COLOR" in globals() else (255, 255, 255)
    pos = (int(self.position.x), int(self.position.y))
    pygame.draw.circle(screen, color, pos, SHOOT_RADIUS, 2)

  def update(self, dt):
    self.position += self.velocity * dt