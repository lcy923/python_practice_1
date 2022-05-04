import pygame


pygame.init()   #초기화 (필수적 요소)


#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Easy Game") #게임 이름
###여기까지만 하면 화면이 떴다가 바로 사라짐

#FPS
clock = pygame.time.Clock()

#배경 이미지
background = pygame.image.load("C:/Users/user/Desktop/PythonWorkspace/pygame_basic/backcolor.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/user/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]         #캐릭터의 가로 크기
character_height = character_size[1]        #캐릭터의 세로 크기
character_x_pos = (screen_width-character_width)/2            #화면의 가로 정중앙
character_y_pos = screen_height-character_height    #화면의 세로 가장 아래부분

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/user/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size  #이미지의 크기를 구해옴
enemy_width = enemy_size[0]         #캐릭터의 가로 크기
enemy_height = enemy_size[1]        #캐릭터의 세로 크기
enemy_x_pos = (screen_width/2)-(enemy_width/2)            #화면의 가로 정중앙
enemy_y_pos = (screen_height/2)-(enemy_height/2)    #화면의 세로 가장 아래부분

#이벤트 루프
running = True  #게임이 진행중인가?
while running:
    dt = clock.tick(60)                 #게임화면의 초당 프레임 수를 설정

#캐릭터 1초동안 100만큼 이동을 해야 함
# 10 fps : 1초 동안 10번 동작 -> 1번에 10만큼 이동
# 20 fps : 1초 동안 5번 동작 -> 1번에 5만큼 이동

    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #창닫기 이벤트가 발생했는가?
            running = False             #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:        #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:      #캐릭터 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:   #캐릭터 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:      #캐릭터 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:    #캐릭터 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP:          #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    #충돌 처리를 위한 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos        #캐릭터의 이동된 위치로 설정

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False                         #충돌시 종료



    #screen.fill((0,0,255))             #배경 색을 (R,G,B)로 채우기
    screen.blit(background, (0,0))      #배경이미지 불러오기    #안되는 이유는 아래에서 해결
    screen.blit(character, (character_x_pos,character_y_pos))   #캐릭터 불러오기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))   #캐릭터 불러오기

    pygame.display.update()             #게임 이미지를 다시 불러와주기


#pygame 종료
pygame.quit()

