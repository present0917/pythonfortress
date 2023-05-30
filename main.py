import pygame
import tank
import block
import bullet


pygame.init()  # 초기화

backgroundColor = (255, 255, 255)  # 배경색 지정
background = [800, 600]  # 배경 해상도
screen = pygame.display.set_mode(background)  # screen을 지정한 해상도로
done = False  # 게임이 끝났는가?
clock = pygame.time.Clock()
tank1 = tank.Tank()

blocks = pygame.sprite.Group()  # 스프라이트의 묶음으로

for _ in range(10):  # 테스트용 10개만
    block_obj = block.Block()
    blocks.add(block_obj)
theBullet = None  # 탄환변수

def running():

    global done, tank1, theBullet  # 캐릭터와 게임오버여부,탄환 전역변수로
    while not done:
        clock.tick(30)  # 30프레임
        screen.fill(backgroundColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        newBullet = tank1.update(pygame.key.get_pressed())  # 키 입력을 받은대로 tank1에 보낸다.
        if newBullet:
            theBullet = newBullet  # 새 탄환
        
        screen.blit(tank1.image, tank1.rect)  # 탱크렌더링
        
        blocks.draw(screen)  # 블럭묶음 렌더링   

        if theBullet:
            theBullet.update()
            if theBullet.rect.y >= background[1]:  # 탄환이 바닥에 닿으면
                theBullet = None  # 탄환을제거
            else:
                screen.blit(theBullet.image, theBullet.rect)  # 탄환렌더링
                
        pygame.display.update()

running()
pygame.quit()  # 종료
