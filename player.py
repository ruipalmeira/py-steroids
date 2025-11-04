from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_COLOR

class Player(CircleShape):
  rotation = 0
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    playerColor = PLAYER_COLOR
    pointList = self.triangle()
    lineWidth = 2
    pygame.draw.polygon(screen, playerColor, pointList, lineWidth)