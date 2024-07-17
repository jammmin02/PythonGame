import pygame
import sys

WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0) # 검은색
CYAN = (2, 255, 255) # 하늘색

def main():
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("첫번째 pygame : 사운드 출력")
    screen = pygame.display.set_mode((800, 600)) # 디스플레이 크기 설정
    clock = pygame.time.Clock() 
    font = pygame.font.Font(None, 40) # 폰트 기본 크기 40

    try: # 예외 처리
        pygame.mixer_music.load("pygame_bgm.ogg") # bgm 로딩
        se = pygame.mixer.Sound("pygame_se.ogg") # se 로딩
    except: # 예외 발생시
        print("ogg 파일이 맞지 않거나, 오디오 기기와 접속되어 있지 않습니다") # 메시지 출력

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        
        key = pygame.key.get_pressed() # 리스트 key에 모든 키 상태 대입
        if key[pygame.K_p] == 1 : # p를 눌렀다면
            if pygame.mixer.music.get_busy() == False : # bgm이 정지 중이라면
                pygame.mixer.music.play(-1) # bgm 재생
                 
            
        if key[pygame.K_s] == 1 : #  s 키를 눌렀다면
            if pygame.mixer.music.get_busy() == True : # bgm이 실행 중이라면
                pygame.mixer.music.stop() # 정지

        if key[pygame.K_SPACE] == 1:
            se.play() # se 재생

        pos = pygame.mixer.music.get_pos() # 변수에 bgm 재생 시간 대입
        txt1 = font.render("BGM pos" + str(pos), True, WHITE) # 재생 시간을 표시 할 surface
        txt2 = font.render("[P]lay bgm : [S]top bgm : [SPACE] se", True, CYAN) # 조작 방법 표시 할 surface
        
        screen.fill(BLACK) # 스크린 색
        screen.blit(txt1, [100, 100]) #스크린에 문자열을 표시한 surface 전송
        screen.blit(txt2, [100, 200])

        pygame.display.update() # 화면 업데이트
        
        clock.tick(10) # 프레임 레이트 지정

if __name__ == '__main__' :
    main()