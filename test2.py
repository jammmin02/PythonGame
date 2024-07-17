import pygame
import sys

WHITE = (255, 255, 255)  # 흰색
BLACK = (0, 0, 0)  # 검은색
CYAN = (0, 255, 255)  # 하늘색

def main():
    pygame.init()  # 모듈 초기화
    pygame.display.set_caption("첫번째 pygame : 사운드 출력")
    screen = pygame.display.set_mode((800, 600))  # 디스플레이 크기 설정
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)  # 폰트 기본 크기 40

    try:  # 예외 처리
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(WHITE)  # 화면을 흰색으로 채우기

            # 여기에 게임 로직이나 화면에 그릴 내용을 추가하세요.
            text = font.render("Hello, Pygame!", True, BLACK)
            screen.blit(text, (200, 300))

            pygame.display.flip()  # 화면 업데이트
            clock.tick(60)  # 초당 프레임 수 설정

    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()