import tkinter
import random

index = 0 # 게임 진행 관리 변수
timer = 0 # 시간 관리 변수
score = 0 # 점수용 변수
hisc = 1000 # 최고 점수용 변수
difficulty = 0 # 난이도 관리 변수
tsugi = 0 # 다음에 놓을 고양이 값 대입 변수

mouse_x = 0  # 마우스 포인터 x 좌표
mouse_y = 0  # 마우스 포인터 y 좌표
mouse_c = 0  # 마우스 포인터 클릭 여부 변수
cursor_x = 0
cursor_y = 0

# 마우스 포인터 이동 시 실행
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

# 마우스 버튼 클릭 시 실행
def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = [] # 칸 관리
check = [] # 판정용
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])

# 고양이 표시 함수
def draw_neko():  
    cvs.delete("NEKO") # 고양이 삭제
    for y in range(10): 
        for x in range(8):
            if neko[y][x] > 0: # 리스트 원소값이 0보다 클 때 고양이 표기
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")

# 고양이가 가로 세로 대각선 3개인지 확인
def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x] # 판정용 리스트에 고양이 값 복사

    #위 아래 같은 고양이라면 발자국으로 변경
    for y in range(1, 9):    
        for x in range(8):
            if check[y][x] > 0:
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    # 좌 우 같은 고양이라면 발자국으로 변경
    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7
                    
    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                #왼쪽 위 오른쪽 아래 같은 고양이라면 발자국으로 변경
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                
                # 왼쪽 아래 오른쪽 위 같은 고양이라면 발자국으로 변경
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

#나란이 놓인 고양이 삭제
def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num += 1
    return num # 지운 수 반환

#고양이 낙하 함수
def drop_neko():
    flg = False #낙하 여부 플래그 (false = 낙하하지 않았음)
    for y in range(8, -1, -1):
        for x in range(8):
            # 고양이 있는 칸 아래가 빈칸이라면
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x] #빈 칸에 고양이 두기
                neko[y][x] = 0 # 원래 있던곳은 빈칸으로
                flg = True # 낙하여부 플래그
    return flg #플래그 값 반환

# 가장 윗줄 도달 여부 확인 함수
def over_neko():
    for x in range(8):
        if neko[0][x] > 0:
            return True # 가장 윗줄에 고양이가 있다면 True 반환
    return False # 없다면 false

# 가장 윗줄에 고양이를 놓는 함수
def set_neko():
    for x in range(8):
        neko[0][x] = random.randint(1, 6)

# 그림자 문자열 표시
def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold") #폰트 지정
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg) #대각선으로 2씩 이동
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg) #지정한 색으로 문자열 표시

#메인처리 함수
def game_main():
    global index, timer, score, tsugi, hisc, difficulty
    global cursor_x, cursor_y, mouse_c
    if index == 0:  # 타이틀 로고
        draw_txt("야옹야옹", 322, 240, 100, "violet", "TITLE")
        
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag = "TITLE")  # 이지 모드
        draw_txt("EASY", 312, 420,40,"White","TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag = "TITLE") # 노말 모드
        draw_txt("Normal", 312, 564, 40,"White","TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag = "TITLE") #하드모드
        draw_txt("Hard", 312, 708, 40,"White","TITLE")
        
        # draw_txt("Click to start", 312, 560, 50, "orange", "TITLE")
        index = 1 
        mouse_c = 0 # 클릭 해제
    
    elif index == 1:  # 타이틀 화면 / 시작 대기
        difficulty = 0
        if mouse_c == 1: # 마우스를 클릭했다면
            if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y < 456: # 이지 모드 선택시
               difficulty = 4
            if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y < 600: # 노말 모드 선택시
               difficulty = 5
            if 168 < mouse_x and mouse_x < 672 and 744 < mouse_y < 456: # 하드 모드 선택시
               difficulty = 6
            
            if difficulty > 0: # 모드 선택 시
                for y in range(10):
                    for x in range(8):
                        neko[y][x] = 0
                mouse_c = 0
                score = 0
                tsugi = 0
                cursor_x = 0
                cursor_y = 0
                set_neko()
                draw_neko()
                cvs.delete("TITLE")
                index = 2
                
    elif index == 2:  # 낙하
        if drop_neko() == False: #고양이 낙하, 낙하할 고양이가 없다면
            index = 3
        draw_neko() # 고양이 표시
    elif index == 3:  # 고양이가 나란히 놓였는가?
        check_neko() 
        draw_neko()
        index = 4
    elif index == 4: # 나란히 놓인 고양이가 있다면 삭제
        sc = sweep_neko() # 발자국 삭제
        score += sc * difficulty * 2 # 발자국 삭제 수를 sc에 대입 후 점수 추가
        if score > hisc: # 최고점 갱신시
            score = hisc #최고점 갱신
        if sc > 0:
            index = 2
        else:
            if over_neko() == False: # 가장 윗줄에 도달하지 않았다면
                tsugi = random.randint(1, difficulty) # 다음에 배치 할 고양이 렌덤 설정
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko() # 고양이 표시
    elif index == 5: # 마우스 입력 대기
        # 마우스 포인터가 좌표 칸 안에 있다면
        if 24 <= mouse_x < 24 + 72 * 8 and 24 <= mouse_y < 24 + 72 * 10: 
            cursor_x = int((mouse_x - 24) / 72) #가로 위치 계산
            cursor_y = int((mouse_y - 24) / 72) #세로 위치 게산
        if mouse_c == 1: # 마우스 버튼 클릭시
            mouse_c = 0 # 클릭 해제
            if neko[cursor_y][cursor_x] == 0:  # 빈칸인지 확인
                neko[cursor_y][cursor_x] = tsugi # 커서 칸에 고양이 배치
                tsugi = 0
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6: # 게임 오버
        timer += 1 # 타이머 값 증가
        if timer == 1: #게임 오버
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50: #리턴
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO") # 점수 삭제
    draw_txt("SCORE" + str(score), 160, 60, 32, "blue", "INFO") # 점수 표시
    draw_txt("HISC" + str(hisc), 450, 60, 32, "yellow", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk() # 윈도우 생성
root.title("낙하 퍼즐 '야옹야옹'") # 윈도우 제목 설정
root.resizable(False, False)  #크기 변경 불가
root.bind("<Motion>", mouse_move)  # 마우스 포인터 이동 시
root.bind("<ButtonPress>", mouse_press)  # 마우스 버튼 클릭 시

cvs = tkinter.Canvas(root, width=912, height=768) # 캔버스 생성
cvs.pack() #캔버스 배치

bg = tkinter.PhotoImage(file="neko_bg.png") # 배경 이미지 
cursor = tkinter.PhotoImage(file="neko_cursor.png") # 커서 이미지

#고양이 이미지 
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
]

cvs.create_image(456, 384, image=bg) # 캠버스에 배경 그리기
game_main() #매인 처리 호출
root.mainloop() #윈도우 표시
