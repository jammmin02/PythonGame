import tkinter

CAT = [
    "전생에 고양이였을 가능성은 매우 낮습니다",
    "보통 사람입니다",
    "특별히 이상한 곳은 없습니다",
    "꽤 고양이다운 구석이 있습니다",
    "고양이와 비슷한 성격 같습니다",
    "고양이와 근접한 성격입니다",
    "전생에 고양이였을지도 모릅니다",
    "겉모습은 사람이지만, 속은 고양이일 가능성이 높습니다"
]

def chick_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True :
            pts += 1
    nekodo = int(100 * pts / 7)
    text.delete("1.0", tkinter.END) # 입력 필드에 생선 된 수를 지우기 위하여
    text.insert("1.0","<진단결과>\n당신의 고양이 지수는" + str(nekodo) + "%입니다.\n" + CAT[pts]) #1.0 = 위젯을 가장 첫번째
    
#윈도우 타이틀 생성
root = tkinter.Tk()
root.title("고양이 지수 진단 게임") 
root.resizable(False,False)

#캠버스 생성
canvas = tkinter.Canvas(root, width = 800, height = 600)
canvas.pack()

#이미지 파일 로딩
gazou = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400, 300, image = gazou)

#버튼 활성화
button = tkinter.Button(text="진단하기", font=("함초롬돋움, 32"), bg="Lightgreen", command=chick_btn)
button.place(x = 400, y = 480)

#텍스트 입력 필드 생성
text = tkinter.Text(width = 40, height = 5, font=("함초롬돋움, 16"))
text.place(x = 320, y = 30)

#체크 버튼용 빈 리스트
bvar = [None] * 7
cbtn = [None] * 7

#질문생성
ITEM = [
    "높은 곳이 좋다",
    "공을 보면 굴리고 싶어진다",
    "깜짝 놀라면 온몸의 털이 곤두선다",
    "쥐구멍이 마음에 든다",
    "개에게 적대감을 느낀다",
    "생선을 좋아한다",
    "밤에 기운이 난다"
]

#반복해서 체크 버튼 배치
for i in range(7):
    
    bvar[i] = tkinter.BooleanVar() 
    bvar[i].set(False) #모든 체크값 false로 설정
    
    #체크버튼 객체 생성
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("함초롬돋움", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160 + 40 * i)

root.mainloop()