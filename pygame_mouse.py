import pygame
import sys # sys 모듈 임포트

BLACK = (0, 0, 0) # 색 정의 흰색 
LBLUE = (0, 192, 255) # 색 정의 : 검은색
PINK = (255, 0, 224) # 색 정의 : 핑크색

def main():
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("첫번째 pygame : 마우스 입력")
    screen = pygame.display.set_mode((800, 600)) # 디스플레이 크기 설정
    clock = pygame.time.Clock() 
    font = pygame.font.Font(None, 60) # 폰트 기본 크기 60

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit() # 프로그램 종료
        
        mouseX, mouseY = pygame.mouse.get_pos() # 마우스 포인터 좌표 대입
        txt1 = font.render("{},{}".format(mouseX,mouseY), True, LBLUE) # 좌표 값을 표시할 surface

        mbtn1, mbtn2, mbtn3 = pygame.mouse.get_pressed() # 변수에 마우스 버튼 상태 대입
        txt2 = font.render("{}:{}:{}".format(mbtn1, mbtn2, mbtn3), True, PINK)  # 마우스 버튼 상태를 표시 할 surface

        screen.fill(BLACK)

        screen.blit(txt1, [100, 100]) # 스크린에 문자 표시
        screen.blit(txt2, [100, 200]) # 스크린에 문자 표시
        
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__' :
    main()