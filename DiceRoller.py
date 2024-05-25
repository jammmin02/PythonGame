import random

pl_pos = 1
com_pos = 1

#주사위 게임 보드 표시하기
def borad():
    print ("-" * (pl_pos - 1) , "p" , "-" * (30-pl_pos) )
    print ("-" * (com_pos - 1) , "c" , "-" * (30-com_pos) )

borad() #보드 세팅
print("주사위 게임을 시작하겠습니다")

#이길 때 까지 반복
while True :
    #사용자 순서
    input("엔터를 누르면 당신의 말이 움직입니다")
   
    pl_pos += random.randint(1,6) #1~6까지 중에 랜덤 숫자 선택
   
    if pl_pos > 30 : # 만약 30보다 크면 30으로 설정
        pl_pos = 30
    
    borad() #보드판 호출
    
    # 30 도달시 게임 종료 후 승리메세지 출력
    if pl_pos == 30 :
        print ("당신이 이겼습니다")
        break
    
    #컴퓨터 순서
    input("엔터를 누르면 컴퓨의 말이 움직입니다")
    com_pos += random.randint(1,6) #1~6까지 중에 랜덤 숫자 선택
   
    if com_pos > 30 : # 만약 30보다 크면 30으로 설정
        com_pos = 30
    
    borad() #보드판 호출
    
    # 30 도달시 게임 종료 후 승리메세지 출력
    if pl_pos == 30 :
        print ("당신이 이겼습니다")
        break
