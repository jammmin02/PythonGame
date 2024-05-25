import tkinter
import tkinter.messagebox
# def click_btn():
#     txt = entry.get()
#     button["text"] = txt


# root=tkinter.Tk()       
# root.title("첫번째 텍스트 입력 필드")
# root.geometry("400x200")
# entry = tkinter.Entry(width=20)
# entry.place(x=20, y=20)

# button = tkinter.Button(text="문자열 얻기", command=click_btn)
# button.place(x=20, y=100)
# root.mainloop()

# def click_but():
#     text.insert(tkinter.END, "몬스터가 나타났다") #문자열 추가위치 설정 
    
# root = tkinter.Tk()
# root.title("여러 행 텍스트 입력")
# root.geometry("400x200")

# button = tkinter.Button(text="메세지", command=click_but)
# button.pack()

# text = tkinter.Text()
# text.pack()
# root.mainloop()

# root =tkinter.Tk()
# root.title("체크버튼 다루기")
# root.geometry("400x200")

# cbtn = tkinter.Checkbutton(text="체크버튼")
# cbtn.pack()
# root.mainloop()

# def check():
#     if cval.get() == True :
#         print("체크되어 있습니다")
#     else :
#         print("체크되어 있지 않습니다") 
    
# root =tkinter.Tk()
# root.title("처음부터 체크 된 상태 만들기")
# root.geometry("400x200")

# cval = tkinter.BooleanVar() #BooleanVar객체 준비
# cval.set(True) #객체 true 설정
# cbtn = tkinter.Checkbutton(text="체크버튼", variable=cval, command=check)
# cbtn.pack()
# root.mainloop()

def chick_btn():
    tkinter.messagebox.showinfo("정보","버튼을 눌렀습니다")

root =tkinter.Tk()
root.title("첫번째 메시지 박스")
root.geometry("400x200")
btn = tkinter.Button(text="테스트",command=chick_btn)
btn.pack()
root.mainloop()