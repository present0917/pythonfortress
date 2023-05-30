import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()
        self.image = pygame.Surface((50,50))  #탄환크기
        self.image.fill((0, 0, 0))  #탄환색
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.Speed = speed

    def update(self):
        self.rect.x += self.Speed[0]
        self.rect.y += self.Speed[1]
        self.Speed[1] += 0.5  # 중력작용
