import tkinter

mouse_x = 0 # 마우스 포인터 x 좌표
mouse_y = 0 # 마우스 포인터 y 좌표
mouse_c = 0 # 마우스 포인터 클릭 여부 변수

# 마우스 포인터 이동시 실행 
def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y
    
#마우스 버튼 클릭 시 실행
def mouse_press(e):
    global mouse_c
    mouse_c = 1

# 마우스 버튼 클릭 후 해제 시 실행 할 함수
def mouse_release(e):
    global mouse_c
    mouse_c = 0

# 실시간 처리
def game_main():
    fnt = ("Times New Roman", 30)
    txt = "mouse({},{}){}".format(mouse_x,mouse_y,mouse_c)
    cvs.delete("TEST")
    cvs.create_text(456, 384, text = txt, fill = "black" , font=fnt, tag="TEST")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("마우스 입력")
root.resizable(False,False) # 윈도우 크기 변경 불가
root.bind("<Motion>", mouse_move) # 마우스 포인터 이동시
root.bind("<ButtonPress>", mouse_press) # 마우스 버튼 클릭시
root.bind("<ButtonRelease>", mouse_release) #마우스 버튼 클릭 후 해제

cvs = tkinter.Canvas(root, width=912, height= 768)
cvs.pack()

game_main()

root.mainloop()
