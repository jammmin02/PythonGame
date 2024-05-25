import tkinter
import random

#버튼 클릭시 실행 될 함수 정의 (제비뽑기 내용)
def click_btn(): 
    Lable["text"] = random.choice(["대길","중길","소길","흉"])
    Lable.update() #문자 변경 즉시 시행

root = tkinter.Tk() #윈도우 객체 생성
root.title("제비뽑기 프로그램") #윈도우 제목 설정
root.resizable(False,False) # 윈도우 크기 고정

canvas = tkinter.Canvas(root, width=800, height=600) #캠버스 컴포넌트 생성
canvas.pack() #윈도우에 캠버스 배치
gazou = tkinter.PhotoImage(file="miko.png") #이미지 파일로드
canvas.create_image(400, 300, image = gazou) #캔버스에 이미지 그리기

#라벨 생성 및 배치 (bg=배경색)
Lable = tkinter.Label(root, text="??", font=("함초롬 돋움", 120), bg= "White")
Lable.place(x = 380, y = 60)

#버튼 생성 및 배치 (fg=문자열 색) command =  함수 호출
button = tkinter.Button(root, text="제비뽑기", font=("함초롬 돋움", 36), command=click_btn ,fg="skyblue" )
button.place(x = 360, y = 400)
root.mainloop()