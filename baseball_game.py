# 게임 목적 : 컴퓨터가 생성한 3개의 난수를 플레이어가 맞춤

# 1 컴퓨터 난수 생성

import random

# 0~9 까지 중에서 3개뽑기
com_list=[] #3개의 난수 저장을 위한 리스트 생성

def k(arg_value, arg_list):
    for i in arg_list:
       if i == arg_value :
        return False
    arg_list.append(arg_value)
    return True

while True:
   com_choice = random.randint(0,9)
   k(com_choice, com_list)
   if len(com_list) ==3 :
      break
      
print(com_list)
      

#2 플레이어 입력

attempt_count = 1 #시도횟수 카운트
out_count = 0 #아웃횟수 카운트

while True:
    player_list=[] #플레이어 입력 숫자 저장 
    print("사용자 입력 :")
    
    for _ in range(3):
        player = int(input())
        player_list.append(player)
    
    attempt_count +=1
    
    #판정하기
    #strike = 자릿수가 같고 "난수값 == 입력 값"일 경우
    #ball = 자릿수가 다르지만 입력값이 난수 값에 있을 경우
    #out = 일치하는 숫자가 아무것도 없을 경우
    
    #strike
    strike_count = 0 #스트라이크 횟수 카운트
    ball_count = 0 #볼 횟수 카운트
    for i in range(3):
        if player_list[i] == com_list[i] :
            strike_count += 1
    #ball   
    if player_list[i] != com_list[i]:   
        for player_num in player_list:
            for com_num in com_list:
                if player_num == com_num and player_list.index(player_num) !=com_list.index(com_num)  :
                    ball_count += 1
    
    #out
    if ball_count == 0 and strike_count == 0 :
        out_count += 1
    
    #결과 출력
    print("스트라이크 :",strike_count,"볼 :",ball_count,"아웃 :", out_count)
    
    #시도 횟수가 5회 초과
    if attempt_count >5 :
       print("게임종료: 패배 (시도횟수 5회 초과)")
       print("정답:",end=" ")
       for answer in com_list:
           print(answer,end=" ")
       break
    
    # out 2회
    elif out_count == 2 :
       print("게임종료: 패배 (out 2회)")
       print("정답:",end=" ")
       for answer in com_list:
           print(answer,end=" ")
       break
    
    # 승리
    elif strike_count == 3 :
        print("게임종료: 승리")
        print("정답:",end=" ")
        for answer in com_list:
           print(answer,end=" ")
        break    