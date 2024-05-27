import tkinter

key = ""

def key_down(e): # 키를 눌렀을 때
    global key
    key = e.keysym

def key_up(e): # 키를 눌렀다 뗐을 때
    global key
    key = ""
    
#캐릭터의 좌표 관리
cx = 400
cy = 300 

#실시간 처리를 위한 함수
def main_proc():
    global cx,cy
    
    if key == "Up" :
        cy -= 20
    if key == "Down" :
        cy += 20
    if key == "Left" :
        cx -= 20
    if key == "Right" :
        cx += 20
    
    canvas.coords("MYCHR",cx ,cy) # 캐릭터를 새로운 위치로 이동
    root.after(100, main_proc)

#윈도우 생성
root = tkinter.Tk()
root.title("캐릭터 이동")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

#캠버스 생성
canvas = tkinter.Canvas(width = 800, height = 600, bg = "Lightgreen" )
canvas.pack()

#사진 불러오기
img =tkinter.PhotoImage(file="mimi.png")
canvas.create_image(cx, cy, image = img, tag = "MYCHR") #캠버스에 이미지 불러오기

main_proc()

root.mainloop()

