import pygame
import sys

WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0) # 검은색

imgBtlbg = pygame.image.load("btlbg.png") # 전투 배경
imgEnemy = pygame.image.load("enemy1.png") # 적 이미지 로딩
emy_x = 440 - imgEnemy.get_width() / 2 # 이미지 폭으로부터 표시 위치(x좌표) 계산
emy_y = 560 - imgEnemy.get_height()    # 이미지 폭으로부터 표시 위치(y좌표) 계산

message = [""] * 10 # 전투 메시지 입력 리스트
def init_message(): 
    for i in range(10): 
        message[i] = "" # 리스트에 빈 문자열 추가

def set_messgae(msg):
    for i in range(10):
        if message[i] == "": # 문자열이 설정되어 있지 않다면
            message[i] = msg # 새로운 문자열 대입
            return
    for i in range(9):
        message[i] = message[i + 1] # 메세지 한 문자씩 슬라이드
    message[9] = msg # 마지막행에 새로운 문자열 대입

def draw_text(bg,txt, x, y, fnt, col): # 문자열 그림자 처리 함수
    sur = fnt.render(txt, True, BLACK) # 검은색으로 문자열 표시 
    bg.blit(sur, [x + 1, y + 2]) # 지정 좌표 약간 오른쪽 아래
    sur = fnt.render(txt, True, col) # 지정한 색으로 문자열 표시 
    bg.blit(sur, [x, y]) # 지정좌표

def draw_battle(bg, fnt): # 전투 화면 표시 함수
    bg.blit(imgBtlbg, [0, 0]) # 배경 표시
    bg.blit(imgEnemy, [emy_x, emy_y]) # 적 표시
    for i in range(10):
        draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE) # 전투 메세지 표시
    
def main(): # 메인 처리 수행 함수
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("전투 개시 처리") # 타이틀
    screen = pygame.display.set_mode((880, 720)) # 스크린 초기화
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    
    init_message()
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # X버튼 누르면 종료
                pygame.quit()
                sys.exit() # 프로그램 종료
            if event.type == pygame.KEYDOWN:
                set_messgae("KEYDOWN" + str(event.key))
                
            draw_battle(screen, font)
            pygame.display.update() 
            clock.tick(5)

if __name__ == '__main__' :
    main()