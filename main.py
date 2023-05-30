import pygame#라이브러리
import block
pygame.init()#초기화

backgroundColor=(255,255,255)#배경색지정
background=[800,600] #배경 해상도
screen=pygame.display.set_mode(background) #screen을 지정한 해상도로
done=False #게임이 끝났는가?
clock=pygame.time.Clock()
tank1=pygame.image.load('images/tank/missile.png')
tank1=pygame.transform.scale(tank1,(80,60))

blocks = pygame.sprite.Group() #스프라이트의 묶음으로

for _ in range(10): #테스트용 10개만
    block_obj = block.Block()
    blocks.add(block_obj)

def running():
    global done,tank1 # 케릭터와 게임오버여부 전역변수로
    x=50
    y=50
    while not done:
        clock.tick(30) #30프레임
        screen.fill(backgroundColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        

        screen.blit(tank1,(x,y))#탱크렌더링   
        blocks.update()  
        blocks.draw(screen) #블럭묶음 렌더링   
        pygame.display.update()


running()
pygame.quit()#종료