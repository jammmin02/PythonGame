import pygame
import sys
import random
from pygame.locals import * # 이벤트 종류나 키보드 상수등에 "pygame" 생략가능

WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0) # 검은색

imgBtlbg = pygame.image.load("btlbg.png") # 전투 배경
imgEffect= pygame.image.load("effect_a.png") # 전투 배경
imgEnemy = pygame.image.load("enemy4.png") # 적 이미지 로딩
emy_x = 440 - imgEnemy.get_width() / 2 # 이미지 폭으로부터 표시 위치(x좌표) 계산
emy_y = 560 - imgEnemy.get_height()    # 이미지 폭으로부터 표시 위치(y좌표) 계산
emy_step = 0 # 적 이동 관리 변수
emy_blink = 0 # 깜빡임 효과
dmg_eff = 0 # 화면 흔들림
COMMAND = ["[A]ttack", "[P]otion", "[B]lazegem", "[R]un"] # 전투명령어 정리

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
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0 : # 화면 흔들림 효과 변수가 설정되있다면
        dmg_eff -= 1 #  변수 1 감소
        bx = random.randint(-20, 20) # x좌표 결정
        by = random.randint(-10, 10) # y좌표 결정
    bg.blit(imgBtlbg, [bx, by]) # 적 표시   
    if emy_blink % 2 == 0:
        bg.blit(imgEnemy, [emy_x, emy_y + emy_step])
    if emy_blink > 0 : # 깜빡임 변수가 설정되있다면
        emy_blink -= 1 # 1 감소
    for i in range(10):
        draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE)

def battle_command(bg, fnt): # 전투 명령어 표시
    for i in range(4):
        draw_text(bg, COMMAND[i], 20, 360 + 60 * i, fnt, WHITE)
    
def main(): # 메인 처리 수행 함수
    global emy_step, emy_blink, dmg_eff
    idx = 10 # 게임 진행 관리 인덱스
    tmr = 0 # 게임 진행 타이머 변수
    
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("턴 처리") # 타이틀
    screen = pygame.display.set_mode((880, 720)) # 스크린 초기화
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    
    init_message()
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # X버튼 누르면 종료
                pygame.quit()
                sys.exit() # 프로그램 종료
        
        draw_battle(screen, font) # 전투 화면 표시
        tmr += 1 # 타이머 값 증가
        key = pygame.key.get_pressed() 
        
        if idx == 10 : # 전투 개시
            if tmr == 1: set_messgae("Encounter!")
            if tmr == 6:
                idx = 11 # 플레이어 입력대기로 이동
                tmr = 0
        
        elif idx == 11 : # 플레이어 입력 대기
            if tmr == 1: set_messgae("Your turn")
            battle_command(screen, font) # 전투 명령어 표시
            if key[K_a] == 1 or key[K_SPACE] == 1 : # 해당 키 누르면
                idx = 12 # 공격으로 이동
                tmr = 0
        
        elif idx == 12 : # 플레이어 공격
            if tmr == 1: set_messgae("Your attack!")
            if 2 <= tmr and tmr <= 4: # tmr 2~4 공격 효과 표시
                screen.blit(imgEffect, [700 - tmr * 120, -100 + tmr * 120])
            if tmr == 5:
                emy_blink = 5 # 적 깜빡임 효과
                set_messgae("***pts of damage!")
            if tmr == 16 :
                idx = 13 # 적 턴으로 이동
                tmr = 0
        
        elif idx == 13 : # 적 턴, 적 공격
            if tmr == 1: set_messgae("Enemy turn.")
            if tmr == 5 :
               set_messgae("Enemy attack!")
               emy_step = 30 # 적 이동 변수 설정 
            if tmr == 9:
                set_messgae("***pts of damage!")
                dmg_eff = 5 # 화면 흔들림
                emy_step = 0 # 적 원래 위치로    
            if tmr == 20 :
                idx = 11 # 플레이어 입력 대기
                tmr = 0        
        
        pygame.display.update() 
        clock.tick(5)

if __name__ == '__main__' :
    main()
            
        
        
            
