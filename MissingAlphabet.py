#사라진 알파벳 찾기 게임

import random
import datetime

# a~z 까지 리스트 생성
def generate_alphabet(start='a', end='z'): #매개 변수 활용 (a~z)까지 출력
    start_ord = ord(start) #ord 문자를 아스키 코드로 변환
    end_ord = ord(end)
    alphabet_list = [chr(i) for i in range(start_ord , end_ord + 1)] # chr은 아스키코들르 문자로 변환
    return alphabet_list


alphabet_list = generate_alphabet(start='a', end='z')

alp_case = ""

#랜덤하게 알파벳 하나를 제거함
alp_choice = random.choice(alphabet_list)

#제거 할 문자를 제외한 알파벳 출력을 위해
for i in alphabet_list :
    if i != alp_choice :
        alp_case += i

print(alp_case) #문제 출력
st = datetime.datetime.now() #첫 입력 시간
user = input("빠진 알파벳을 입력하세요 : ")

if user == alp_choice :
    et = datetime.datetime.now() #답을 입력한 시간계산
    print ("정답입니다")
    print (str((et-st).seconds),"초입니다") #초 단위로 출력하기위해
else :
    print ("틀렸습니다")