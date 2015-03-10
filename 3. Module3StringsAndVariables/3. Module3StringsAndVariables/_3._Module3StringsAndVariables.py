# -*- coding: cp949 -*-
name = input("What is your name ? ")    # name이라는 변수 안에 값을 대입
print(name)                             # name에 지정된 변수값 출력
name = "ABC"                            # name을 ABC라고 지정
print(name)                             # name에 지정된 변수값 출력


#
print("\n\n ---------------------- \n\n")
#


#print("What is your name?")             # 다른 방법. 커서가 아랫줄로 이동.
#name = input()
#print(name)

#변수의 특징: 띄어쓰기가 안된다.
#            *대소문자를 구별한다. 명령어, 변수 둘 다 동일적용.
#             숫자로 시작할 수 없다.
#            *date라는 변수명은 사용하지 말기.

#메세지 입력/출력
message = input("Please input Message ")
print(message)
#대/소문자를 바꿈
message = message.swapcase()
print(message)
#전부 대문자로
message = message.upper()
print(message)
#전부 소문자로
message = message.lower()
print(message)

#더 간단한 코드
#print(message.swapcase())
#print(message.lower())
#print(message.upper())

print("\n\n ---------------------- \n\n")

#윈도우 커맨드 상의 cls를(화면 클리어) 파이썬으로 가져오는 방법.
#구글링으로 찾음
#import os
#os.system("cls")

name = input("What is your name?\n")
country = input("What country do you live in?\n")
country = country.upper()
print(name + ", You live in " + country + "!")


#
print("\n\n ---------------------- \n\n")
#


note = "abcdacc"
print(note)

#c가 몇번째에 나오는지 알려줌.
#위 같은 경우, a b c d a c c
#              0 1 2 3 4 5 6 이라서 2 출력
print(note.find("c"))

#c가 몇개 있는지 세어줌
print(note.count("c"))

#제일 앞글자를 대문자로 변환해줌
print(note.capitalize())
#a를 f로 바꿔줌
print(note.replace("a" , "f"))
