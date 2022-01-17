import pygame
###########################################################################
#기본 초기화!
pygame.init() #초기화
#화면크기
screen_width = 480 #가로크기
screen_height = 600 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Gyuddi game") #게임이름

#FPS
clock = pygame.time.Clock()
############################################################################

# 1. 사용자 게임 초기화(배경,케릭터,폰트,좌표,속도 등 설정)

running = True #게임이 진행중인가
while running:
    dt = clock.tick(60) #게임의 초당 프레임

    # 2. 이벤트 처리(키보드 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트인가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생했는가?
            running = False

    #3. 게임케릭터 위치

    #4.충돌처리

    #5.화면에 그리기

    pygame.display.update() #게임화면 다시그리기
pygame.quit()