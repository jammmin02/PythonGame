import random

def getRandList(argNumRandValues, argStartValue, argEndValue):
    # 컴퓨터가 생성한 랜덤 값을 저정하기 위한 리스트
    # 1 - 10 사이 유일한 값 3개를 생성 후 저장
    random_list = []

    # 현재 생성된 랜덤 값의 개수 : 0 -> 2
    rand_trial_count = 0

    # 랜덤 값 3개를 생성하기 위해 while문 사용
    while rand_trial_count < argNumRandValues:
        
        # 랜덤 값 생성
        rand_value = random.randint(argStartValue, argEndValue)
        
        # 중복 값 확인을 위한 플래그 변수
        found_dup_value = False
        
        # 중복값 검사를 위한 반복문 : 반복회수 현재 N번째 -> N-1
        for index in range(rand_trial_count):
            if random_list[index] == rand_value:
                found_dup_value = True
                break
            
        # 생성된 랜덤 값이 중복되지 않을 경우
        if not found_dup_value:
            random_list.append(rand_value) # 리스트에 랜덤 값을 추가
            rand_trial_count += 1 # 다음 랜덤 값 생성 실행
            
    return random_list
            
com_random_list = getRandList(3, 1, 3)

print("컴퓨터 랜덤 값: ", com_random_list)

count_game_trial = 0
count_strike_out = 0

while True:
    count_strkie = 0
    count_ball = 0
    
    # 사용자 입력
    print("사용자 입력 : ")
    user_input = [int(input()) for _ in range(3)]
    
    # strkie, ball 판정
    for i in range(3):
        for j in range(3):
            if com_random_list[i] == user_input[j]:
                if i == j:
                    count_strkie += 1
                else:
                    count_ball += 1
                
                break
            
    # 스트라이크 아웃
    if count_strkie == 0 and count_ball == 0:
        count_strike_out += 1
        print("스트라이크 아웃")
    else:
        print("Strike: ", count_strkie, "\tBall: ", count_ball)
        
    # 종료 조건
    # 1) Lose
    #   - 시도 회수 5번 이상
    #   - 스트라이크 아웃 2번 이상
    if count_game_trial >= 5 or count_strike_out >= 2:
        msg = "5회 이상 실행" if count_game_trial >= 5 else "스트라이크 아웃 2회 이상"
        print(msg, "\t 게임 종료")
        break
    
    # 2) Win
    #   - strike 3개
    if count_strkie >= 3:
        print("승리\t게임 종료")
        break

