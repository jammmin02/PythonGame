import pygame
import sys # sys 모듈 임포트

WHITE = (255, 255, 255) # 색 정의 흰색 
BLACK = (0, 0, 0) # 색 정의 : 검은색

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("첫번째 Pygame") # 윈도우 타이틀 정의 
    screen = pygame.display.set_mode((800, 600)) # 스크린 초기화
    clock = pygame.time.Clock() # dock 오브젝트 초기화
    font = pygame.font.Font(None, 80) # font 오브젝트 초기화
    tmr = 0 # 시간 관리 변수 tmr 선언
    
    while True: # 무한 반복
        tmr += 1  # tmr값 1 증가
        for event in pygame.event.get(): # 이벤트 반복
            if event.type == pygame.QUIT : # X버튼 누르면 종료
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 프로그램 종료
        
        txt = font.render(str(tmr), True, WHITE) # surface에 문자열 표시
        screen.fill(BLACK) # 지정한 색으로 스크린 채움
        screen.blit(txt,[300, 200]) # 문자열 표시한 surface를 스크린으로 전송
        pygame.display.update() # 화면 업데이트
        clock.tick(10) # frameate 지정
        
if __name__ == '__main__' : # 이프로그램 직접 실행시
    main() # 함수 호출