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
tanks = [tank.Tank(1), tank.Tank(2)]  # 탱크가 두개가됐다.
nowPlayer=0 #0번플레이어부터 시작
blocks = pygame.sprite.Group()  # 스프라이트의 묶음으로

for _ in range(10):  # 테스트용 10개만
    block_obj = block.Block()
    blocks.add(block_obj)
theBullet = None  # 탄환변수

def running():

    global done, tanks, theBullet,nowPlayer  # 캐릭터와 게임오버여부,탄환 전역변수로
    while not done:
        clock.tick(30)  # 30프레임
        screen.fill(backgroundColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        exist=theBullet is not None
        newBullet = tanks[nowPlayer].update(pygame.key.get_pressed(),blocks,exist)  # 키 입력을 받은대로 탱크에 보낸다.
        if newBullet and not exist:
            theBullet = newBullet  # 새 탄환
        
        # for i,tank in enumerate(tanks):  # 
        #     screen.blit(tank.image, tank.rect)  # 탱크렌더링
        
        for tank in tanks:
            tank.flip(screen) 
        
        
        blocks.draw(screen)  # 블럭묶음 렌더링   

        if theBullet:
            theBullet.update()
            if theBullet.rect.y >= 600:  # 탄환이 바닥에 닿으면
                theBullet = None  # 탄환을제거
                nowPlayer = (nowPlayer + 1) % 2  # 턴넘김
            else:
                for i, tank in enumerate(tanks):  # hit체크
                    if theBullet.rect.colliderect(tank.rect) and i != nowPlayer:  # 상대에 탄맞으면
                        tank.hiten()  # 체력까기
                        theBullet = None  # 탄환제거
                        nowPlayer = (nowPlayer + 1) % 2  # 턴넘김
                        break
                if theBullet:  # 아직탄환 날라가는중이면
                    screen.blit(theBullet.image, theBullet.rect)  # 렌더링
                
        pygame.display.update()

running()
pygame.quit()  # 종료
