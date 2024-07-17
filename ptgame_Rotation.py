import pygame

WHITE = (255, 255, 255)
NAVY = (0, 0, 128) # 남색


def main():
    pygame.init()
    pygame.display.set_caption("첫번째 Pygame: 화면 회전, 확대/축소")
    screen = pygame.display.set_mode((600, 400)) # 디스플레이 크기 설정
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    img = pygame.image.load("pg_slime.png") # 사진 불러 오기
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # x 누르면 종료
                pygame.quit()

        ang = (tmr % 36) * 10 # 회전각
        per = (tmr % 100) / 20 # 확대 비율
        img_s = pygame.transform.scale(img, [70, 92]) # 확대 
        img_r = pygame.transform.rotate(img, ang) # 회전
        img_rz = pygame.transform.rotozoom(img, ang, per) #회전하면서 확대

        screen.fill(NAVY) # 디스플레이 남색
        # 이미지 표시
        screen.blit(img, [100, 100])
        screen.blit(img_s, [200, 100])
        screen.blit(img_r, [300, 100])
        screen.blit(img_rz, [400, 100])

        txt = font.render(str(tmr), True, WHITE) # 타이머 색상
        screen.blit(txt, [50, 50]) # 타이머 표시

        pygame.display.update() # 디스플레이 업데이트
        clock.tick(10) # 프레임 설정


if __name__ == '__main__':
    main()