import pygame
import sys

WHITE = (255, 255, 255) # 흰색

imgBtlbg = pygame.image.load("btlbg.png") # 전투 배경
imgEnemy = None # 적 이미지 로딩 할 변수

emy_num = 0 # 로딩할 이미지 번호 관리 변수

emy_x = 0 # 적 위치 x좌표
emy_y = 0 # 적 위치 y좌표

def init_battle(): # 전투 개시 준비 함수
    global imgEnemy, emy_num, emy_x, emy_y 
    emy_num += 1 # 관리 번호 증가
    if emy_num == 5: # 관리번호가 5라면
        emy_num = 1 # 관리 번호 1로 되돌림
    imgEnemy = pygame.image.load("enemy" + str(emy_num) + ".png" ) # 적 이미지 로딩
    emy_x = 440 - imgEnemy.get_width() / 2 # 이미지 폭으로부터 표시 위치(x좌표) 계산
    emy_y = 560 - imgEnemy.get_height()    # 이미지 폭으로부터 표시 위치(y좌표) 계산
    
def draw_battle(bg, fnt): # 전투 화면 표시 함수
    bg.blit(imgBtlbg, [0, 0]) # 배경 표시
    bg.blit(imgEnemy, [emy_x, emy_y]) # 적 표시
    sur = fnt.render("enemy" + str(emy_num) + ".png", True, WHITE) # 파일명 표시  surface
    bg.blit(sur, [360, 580]) # 문자열 표시한 surface 화면으로 전송
    
def main(): # 메인 처리 수행 함수
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("전투 개시 처리") # 타이틀
    screen = pygame.display.set_mode((880, 720)) # 스크린 초기화
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    
    init_battle() # 전투 개시 함수 호출
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # X버튼 누르면 종료
                pygame.quit()
                sys.exit() # 프로그램 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # 스페이스 키 누르면
                    init_battle() # 함수 호출
        
        draw_battle(screen, font) # 전투화면 표시
        pygame.display.update() 
        clock.tick(5)

if __name__ == '__main__' :
    main()