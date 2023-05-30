import pygame

class Hpbar:
    def __init__(self, x, y, total):
        self.x = x
        self.y = y#체력바위치
        self.total = total#최대값
        self.current = total
        self.bar_length = 200
        self.bar_height = 20# 체력바 크ㄱㅣ

    def decrease(self, amount):
        self.current -= amount
        if self.current < 0:
            self.current = 0

    def draw(self, surface):
        current_length = self.bar_length * (self.current / self.total)
        border_rect = pygame.Rect(self.x, self.y, self.bar_length, self.bar_height)
        inner_rect = pygame.Rect(self.x, self.y, current_length, self.bar_height)
        pygame.draw.rect(surface, (255, 0, 0), border_rect, 2)  # 테두리렌더링
        pygame.draw.rect(surface, (0, 255, 0), inner_rect)  #현재체력으로다시렌더링
