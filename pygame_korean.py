import pygame
import sys

WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0) # 검은색

def main():
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("첫번째 pygame : 한국어 표시하기")
    screen = pygame.display.set_mode((800, 600)) # 디스플레이 크기 설정
    clock = pygame.time.Clock() 
    font = pygame.font.SysFont("malgungothic", 80) # 시스템 폰트 사용 시
    # font = pygame.font.Font("{font_path/{font_name}.ttf}", 80) # 별도 폰트 사용시

    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

        txt = font.render("한국어 표시 " + str(tmr), True, WHITE)   
        screen.fill(BLACK)
        screen.blit(txt, [100, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__' :
    main() 