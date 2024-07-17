import pygame
import sys
import random

CYAN = (0, 255, 255) # 하늘색
GRAY = (96, 96, 96) # 회색

MAZE_W = 11 # 미로 가로 방향 길이 (가로 칸 수)
MAZE_H = 9 # 미로 세로 방향 길이 (세로 칸 수)

maze = [] # 미로 데이터 관리 리스트

for y in range(MAZE_H): # 반복
    maze.append([0] * MAZE_W) # 리스트 초기화

def make_maze() : # 미로 생성 함수
    XP = [0, 1, 0, -1] # 기둥에서 벽을 그리기 위한 값 정의
    YP = [-1, 0, 1, 0]

    # 주변 벽
    for x in range(MAZE_W): # 노션 미로 설명 참조
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1

    # 안을 아무것도 없는 상태로 
    for y in range(1, MAZE_H - 1): 
        for x in range(1, MAZE_W - 1):
            maze[y][x] = 0
    
    # 기둥
    for y in range(2, MAZE_H - 2, 2): 
        for x in range(2, MAZE_W - 2, 2):
            maze[y][x] = 1

    # 기둥에서 상하좌우로 벽 생성
    for y in range(2, MAZE_H - 2, 2): 
        for x in range(2, MAZE_W - 2, 2):
            d = random.randint(0, 3)
            if x > 2: # 2번째 열부터 왼쪽으로는 벽을 만들지 않음
                d = random.randint(0, 2)
            maze[y + YP[d]][x + XP[d]] = 1

def main(): # 메인 처리 수행 함수
    pygame.init() # 모듈 초기화
    pygame.display.set_caption("미로 생성") # 타이틀
    screen = pygame.display.set_mode((528, 432)) # 스크린 초기화
    clock = pygame.time.Clock()

    make_maze() # 미로 생성 호출

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # X버튼 누르면 종료
                pygame.quit()
                sys.exit() # 프로그램 종료
            if event.type == pygame.KEYDOWN: # 키를 눌렀을 떄
                if event.key == pygame.K_SPACE: # 스페이스 키라면 미로 생성 
                    make_maze()
        
        for y in range(MAZE_H): # 2중 반복
            for x in range(MAZE_W): # 반복해서 미로 표시
                W = 48 # 1칸의 폭
                H = 48 # 1칸의 높이
                X = x * W # 표시 할 x 좌표 계산
                Y = y * H # 표시 할 Y 좌표 계산
                if maze[y][x] == 0: # 미로
                    pygame.draw.rect(screen, CYAN, [X, Y, W, H])
                if maze[y][x] == 1: # 벽
                    pygame.draw.rect(screen, GRAY, [X, Y, W, H])
        
        pygame.display.update() # 화면 업데이트
        clock.tick(2) # 프레임 설정

if __name__ == '__main__' :
    main()

                