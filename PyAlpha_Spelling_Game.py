#게임 목적

#1. 3개의 영단어 입력받기
#1-1. 단어 범위는 5~20 이하
#1-2. 범위 벗어나면 재입력 요구
import random
word_list=[]

def get_Word():
    num = 1
    while True:
        word = input(f"{num}번째 단어를 입력하세요: ")
        if len(word) < 5 or len(word) >20 :
            print("다시 입력하세요")
        else:
            word_list.append(word)
            num += 1
        if len(word_list) == 3 :
            break

get_Word()

#2. 3개의 단어 중 하나 선택
#2-1. 선택 된 단어 리스트화
word_choice = random.choice(word_list)
choice_list = list(word_choice)

#3. 단어 blind 처리하기
#3-1. 올림 처리
if len(choice_list) % 2 != 0 :
    blind_num = ((len(choice_list) // 2) + 1)
else :
    blind_num = len(choice_list) // 2 

#3-2. blind 알파벳 선택
blind_list= []
indexs=[]
for _ in range(blind_num):
    blind_index = random.randint(0,len(choice_list)-1)
    while choice_list[blind_index] == "_" :
        blind_index = random.randint(0,len(choice_list)-1)
    indexs.append(blind_index)
    blind_list.append(choice_list[blind_index])
    choice_list[blind_index] = "_"

print(blind_list)
print(indexs)

# 3-3 블라인드 처리 된 알파벳 출력하기

print("단어 선택 완료 게임을 시작합니다. 선택된 단어: ","".join(choice_list))

num_count = 0
while True:
    user = input("아래 단어를 구성하는 알파벳 한 개를 입력하세요: ")

    count = 0  # count 변수를 초기화

    for a in range(len(blind_list)):
        if blind_list[a] == user :
            count += 1
            choice_list[indexs[a]] = user
            blind_list[a] = "_"

    num_count += 1
    print("입력한 알파벳 단어 내 포함 : ",count)
    print("현재 단어 상태:", "".join(choice_list))
    
    if count == 0 :
        num_count += 1
        print("단어 내 포함되지 않은 알파벳입니다")
        print("현재 단어 상태:", "".join(choice_list))
    
#4-3. 입력받은 알파벳이 있다면 블라인드 해제 

    if all(char == "_" for char in blind_list):
        print("게임 종료")
        print("정답 :","".join(choice_list),"총 시도 횟수 :",num_count)
        break



    

