import pygame


pygame.init()   #초기화 (필수적 요소)


#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Easy Game") #게임 이름
###여기까지만 하면 화면이 떴다가 바로 사라짐

#이벤트 루프
running = True  #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #창닫기 이벤트가 발생했는가?
            running = False             #게임이 진행중이 아님

#pygame 종료
pygame.quit()
