#################################################################################################################################
# from lib2to3.pgen2.pgen import PgenGrammar


# 하늘에서 떨어지는 상자 피하는 게임

# [조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 상자는 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. fps는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640*480(세로 가로) - background.png
# 2. 캐릭터 : 70*70 - character1.png
# 3. 상자 : 70*70 - enemy.png
#################################################################################################################################
import random
import pygame

pygame.init()       #초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("상자 피하기")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/user/Desktop/PythonWorkspace/pygame_basic/backcolor.png")

character = pygame.image.load("C:/Users/user/Desktop/PythonWorkspace/pygame_basic/character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width-character_width)/2
character_y_pos = screen_height-character_height

to_x = 0


character_speed = 0.3

enemy = pygame.image.load("C:/Users/user/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0,screen_width - character_width)
enemy_y_pos = -enemy_height

game_font = pygame.font.Font(None, 40)

running = True
while running:

    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:          #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    enemy_y_pos += 0.3 * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height - enemy_height :
        enemy_y_pos = -enemy_height
        enemy_x_pos = random.randint(0,screen_width - character_width)



    #충돌 처리를 위한 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False                         #충돌시 종료


    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    pygame.display.update()             #게임 이미지를 다시 불러와주기

#종료 직전 2초 대기
pygame.time.delay(2000)

#pygame 종료
pygame.quit()
