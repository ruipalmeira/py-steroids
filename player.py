from circleshape import *
from shoot import *
from constants import PLAYER_RADIUS, PLAYER_COLOR, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED

class Player(CircleShape):
  rotation = 0
  shot_cooldown = 0
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
  
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt
  
  def update(self, dt):
    # decrement shot_cooldown
    if self.shot_cooldown > 0:
      self.shot_cooldown = max(0.0, self.shot_cooldown - dt)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.rotate(-dt)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)
    if keys[pygame.K_SPACE]:
      self.shoot()

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt
    
  def shoot(self):
    if(self.shot_cooldown <= 0):
      shot = Shoot(self.position.x, self.position.y, self.radius)
      velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
      shot.velocity = velocity
      self.shot_cooldown = PLAYER_SHOOT_COOLDOWN 
    