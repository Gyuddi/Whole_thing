import pygame

pygame.init() #초기화
#화면크기
screen_width = 480 #가로크기
screen_hight = 600 #세로
screen = pygame.display.set_mode((screen_width, screen_hight))

#화면 타이틀
pygame.display.set_caption("Gyuddi game") #게임이름


# 배경이미지 불러오기
background = pygame.image.load("C:/Users/한규현/Desktop/기타/pythonworkspace/pygame_basic/background.png")

#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #어떤 이벤트인가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생했는가?
            running = False

    screen.blit(background,(0,0))  #배경 그리기

    pygame.display.update() #게임화면 다시그리기       
 #게임종료
pygame.quit()