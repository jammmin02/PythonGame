import tkinter
import tkinter.messagebox

key = "" 
#키를 눌렀을 때 함수 실행 할 함수 정의
def key_down(e): # 키를 눌렀을 때
    global key
    key = e.keysym

def key_up(e): # 키를 눌렀다 뗏을 때
    global key
    key = ""

mx = 1 #캐릭터의 가로 방향
my = 1 #캐릭터의 새로 방향
yuka = 0 # 칠해진 칸을 세는 함수

# 실시간 처리 수행
def main_proc() :
    global mx , my , yuka
    
    if key == "Shift_L" and yuka > 1 :
        canvas.delete("PAINT")
        mx = 1
        my = 1
        yuka = 0
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2 :
                    maze[y][x] = 0
    
    if key == "Up" and maze[my - 1][mx] == 0 :
        my -= 1
    if key == "Down" and maze[my + 1][mx] == 0 :
        my += 1
    if key == "Left" and maze[my][mx - 1] == 0 :
        mx -= 1
    if key == "Right" and maze[my][mx + 1] == 0 :
        mx += 1
    if maze[my][mx] == 0 : # 캐릭터가 있는 장소라면 2로 변경 
        maze[my][mx] = 2
        yuka += 1
        # 해당 위치를 분홍색으로 변경
        canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="pink", width=0, tags="PAINT")
        canvas.delete("MYCHR")
        canvas.create_image(mx * 80 + 40, my * 80 + 40, image = img, tag = "MYCHR")

    if yuka == 30:
        canvas.update()  # 캔버스 업데이트
        tkinter.messagebox.showinfo("축하합니다!!", "모든 바닥을 칠했습니다")
    else:  # 실패 시 다시 실행할 함수 지정
        root.after(100, main_proc)

root = tkinter.Tk()
root.title("미로를 칠한다냥")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

# 미로 생성
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

for y in range(7): # 세로 반복
    for x in range(10): #가로 반복
        if maze[y][x] == 1 :
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill="skyblue", width=0)

# 사진 불러오기
img = tkinter.PhotoImage(file= "mimi_s.png")
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag = "MYCHR")
main_proc()

root.mainloop()