import pygame
import sys
import random

CYAN = (0, 255, 255) # 하늘색
GRAY = (96, 96, 96) # 회색
BLACK = (0, 0, 0) # 검은색

MAZE_W = 11 # 미로 가로 방향 길이 (가로 칸 수)
MAZE_H = 9 # 미로 세로 방향 길이 (세로 칸 수)

maze = [] # 미로 데이터 관리 리스트

for y in range(MAZE_H): # 반복
    maze.append([0] * MAZE_W) # 리스트 초기화

DUNGEON_W = MAZE_W * 3  # 던전 가로 방향 길이 (가로 칸 수)
DUNGEON_H = MAZE_H * 3  # 던전 가로 방향 길이 (가로 칸 수)

dungeon = []

for y in range(DUNGEON_H): # 반복
    dungeon.append([0] * DUNGEON_W) # 리스트 초기화

imgWall = pygame.image.load("wall.png") # 벽 이미지
imgFloor = pygame.image.load("floor.png") # 통로 이미지

def make_dungeon() : # 던전 자동 생성
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
    
    # 미로에서 던전 생성
    # 전체를 벽으로 만듬
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9 # 던전 값을 모두 9(벽)으로 설정
    
    # 방과 미로 배치
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            dx = x * 3 + 1
            dy = y * 3 + 1
            if maze[y][x] == 0: # 미로 데이터 확인, 칸이 길이라면
                if random.randint(0, 99) < 20 : # 방 생성 여부를 무작위로 결정
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy + ry][dx + rx] = 0 # 3 * 3 칸을 방으로 만듬
                else : # 통로 생성 (방을 만들지 않는 경우 통로 생성)
                    dungeon[dy][dx] = 0 # 3 * 3 중앙을 통로로
                    if maze[y - 1][x] == 0: # 미로 위 칸이 길이라면
                        dungeon[dy - 1][dx] = 0 # 통로를 위로 연장
                    if maze[y + 1][x] == 0: # 미로 아래 칸이 길이라면
                        dungeon[dy + 1][dx] = 0 # 통로를 아래로 연장
                    if maze[y][x - 1] == 0: # 미로 왼쪽이 길이라면
                        dungeon[dy][dx - 1] = 0 # 통로를 왼쪽으로 연장
                    if maze[y][x + 1] == 0: # 미로 오른쪽이 길이라면
                        dungeon[dy - 1][dx + 1] = 0 # 통로를 오른쪽으로 연장
