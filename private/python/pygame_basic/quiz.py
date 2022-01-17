import pygame
import random
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


background = pygame.image.load("C:/Users/한규현/Desktop/기타/pythonworkspace/pygame_basic/background.png")

character = pygame.image.load("C:/Users/한규현/Desktop/기타/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) #화면 중간에 위치
character_y_pos = screen_height-character_height #화면 가장 아래

to_x = 0
to_y = 0

character_speed = 0.6


enemy = pygame.image.load("C:/Users/한규현/Desktop/기타/pythonworkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,480) #무작위 좌표
enemy_y_pos = 0 #화면 밖에서 떨어짐


#폰트정의
game_font = pygame.font.Font(None,40)

#총 시간
total_time = 10

#시작 시간 정보
start_ticks = pygame.time.get_ticks()



running = True #게임이 진행중인가
while running:
    dt = clock.tick(60) #게임의 초당 프레임


    # 2. 이벤트 처리(키보드 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트인가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생했는가?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:          
             if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
        


    character_x_pos += to_x * dt
    enemy_y_pos += character_speed* dt
    #3. 게임케릭터 위치
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 

    if enemy_y_pos > 530:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,480)

    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos


    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    #5.화면에 그리기

    
    screen.blit(background,(0,0))  #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos))

    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))


    pygame.display.update() #게임화면 다시그리기
pygame.quit()