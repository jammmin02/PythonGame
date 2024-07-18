import pygame
import sys
import random

WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0) # 검은색

def main(): # 메인 처리 수행 함수
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("반투명과 스크롤") # 타이틀
    screen = pygame.display.set_mode((800, 600)) # 스크린 초기화
    clock = pygame.time.Clock()
    
    surface_a = pygame.Surface((800,600))
    surface_a.fill(BLACK)
    surface_a.set_alpha(32) # 투명도 설정
    
    CHIP_MAX = 50 # 광탄 수
    cx = [0] * CHIP_MAX # 광탄 x 좌표
    cy = [0] * CHIP_MAX # 광탄 y 좌표
    xp = [0] * CHIP_MAX # 광탄 x 방향 이동량
    yp = [0] * CHIP_MAX # 광탄 y 방향 이동량
    
    for i in range(CHIP_MAX):
        cx[i] = random.randint(0, 800) # 광탄 x좌표 결정
        cy[i] = random.randint(0, 600) # 광탄 y좌표 결정
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # X버튼 누르면 종료
                pygame.quit()
                sys.exit() # 프로그램 종료
            
        screen.scroll(1, 4) #  화면에 그린 이미지 이동 (스크롤)
        screen.blit(surface_a, [0, 0]) # 화면에 검은 반투명 surface 겹침
        
        mx, my = pygame.mouse.get_pos() # 마우스 포인터 좌표 대입
        pygame.draw.rect(screen, WHITE, [mx - 4, my - 4, 8, 8]) # 마우스 포인터 좌표에 사각형 표시
        
        for i in range(CHIP_MAX): # 반복해소 광탄 이동
            if mx < cx[i] and xp[i] > -20: xp[i] -= 1  # 마우스 포인터 좌표
            if mx > cx[i] and xp[i] < 20: xp[i] += 1   # 광탄 좌표 비교
            if my < cy[i] and yp[i] > -16: yp[i] -= 1  # x방향과 y방향 이동량
            if my > cy[i] and yp[i] < 16: yp[i] += 1   # 변경
            
            cx[i] += xp[i] # x 좌표 변경
            cy[i] += yp[i] # y 좌표 변경
            
            pygame.draw.circle(screen, (0, 64, 192), [cx[i], cy[i]], 12)
            pygame.draw.circle(screen, (0, 128, 224), [cx[i], cy[i]], 9)
            pygame.draw.circle(screen, (192, 224, 255), [cx[i], cy[i]], 6)
            
        pygame.display.update() 
        clock.tick(30)

if __name__ == '__main__' :
    main()
            
           