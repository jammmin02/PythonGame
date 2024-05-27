import tkinter

key = 0 # 키코드 입력변수 선언

def key_down(e):
    global key #전역변수 선언
    key = e.keycode #눌려진 키의 코드를 key에 대입
    print ("KEY:", str(key))

root = tkinter.Tk()
root.title("키코드 얻기")
root.bind("<KeyPress>", key_down) #bind()명령으로 키를 눌렀을 때 실행 할 함수지정
root.mainloop()

#<KeyPress>,<Key> = 키를 누름
#<KeyRelease> = 키를 눌렀다 뗌
#<Motion> = 마우스 포인터 움직임
#<ButtonPresss>,<Button> = 마으스 버튼 클릭