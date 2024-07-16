import pygame
import sys
import math

WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0) # 검은색
RED = (255, 0, 0) # 빨간색
GREEN = (0 ,255, 0) # 초록색
BLUE = (0, 0, 255) # 파란색
GOLD = (255, 216, 0) # 금색
SILVER = (192, 192, 192) # 은색
COPPER = (192, 112, 48) # 동색

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("첫번재 pygame: 도형") # 타이틀 지정
    screen = pygame.display.set_mode((800,600)) # 스크린 초기화
    clock = pygame.time.Clock() # clock 초기화
    tmr = 0 # 타이머
    
    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # x 누르면 종료
                pygame.quit() # 초기화 해제
                sys.exit() # 프로그램 종료
        
        screen.fill(BLACK)
        
        pygame.draw.line(screen, RED, [0, 0], [100,200], 10) # 선표시
        pygame.draw.lines(screen, BLUE, False, [[50, 300], [150, 400], [50, 500]]) # 선표시
        pygame.draw.rect(screen, RED, [200, 50, 120,80]) # 사각형
        pygame.draw.rect(screen, GREEN, [200, 200, 60, 180], 5) # 사각형
        pygame.draw.polygon(screen, BLUE, [[250, 400], [200, 500], [300, 500]], 10) # 다각형 표시
        pygame.draw.circle(screen, GOLD, [400,100],60) # 원표시
        pygame.draw.ellipse(screen, SILVER, [400 - 80, 300 - 40, 160, 80]) # 타원 표시
        pygame.draw.ellipse(screen,COPPER, [400 - 40, 500 - 80, 80, 160], 20) # 타원 표시
        
        ang = math.pi * tmr / 36 # 원호 각도 계산
        pygame.draw.arc(screen, BLUE, [600 - 100, 300 - 200,  200, 400], 0, math.pi * 2) # 원호 표시
        pygame.draw.arc(screen, WHITE, [600 - 100, 300 - 200,  200, 400], ang, ang + math.pi / 2, 8) # 원호 표시
        
        pygame.display.update() #화면 업데이트
        clock.tick(10)

if __name__ == '__main__' :
    main()