# -*- coding: cp949 -*-
name = input("What is your name ? ")    # name�̶�� ���� �ȿ� ���� ����
print(name)                             # name�� ������ ������ ���
name = "ABC"                            # name�� ABC��� ����
print(name)                             # name�� ������ ������ ���


#
print("\n\n ---------------------- \n\n")
#


#print("What is your name?")             # �ٸ� ���. Ŀ���� �Ʒ��ٷ� �̵�.
#name = input()
#print(name)

#������ Ư¡: ���Ⱑ �ȵȴ�.
#            *��ҹ��ڸ� �����Ѵ�. ��ɾ�, ���� �� �� ��������.
#             ���ڷ� ������ �� ����.
#            *date��� �������� ������� ����.

#�޼��� �Է�/���
message = input("Please input Message ")
print(message)
#��/�ҹ��ڸ� �ٲ�
message = message.swapcase()
print(message)
#���� �빮�ڷ�
message = message.upper()
print(message)
#���� �ҹ��ڷ�
message = message.lower()
print(message)

#�� ������ �ڵ�
#print(message.swapcase())
#print(message.lower())
#print(message.upper())

print("\n\n ---------------------- \n\n")

#������ Ŀ�ǵ� ���� cls��(ȭ�� Ŭ����) ���̽����� �������� ���.
#���۸����� ã��
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

#c�� ���°�� �������� �˷���.
#�� ���� ���, a b c d a c c
#              0 1 2 3 4 5 6 �̶� 2 ���
print(note.find("c"))

#c�� � �ִ��� ������
print(note.count("c"))

#���� �ձ��ڸ� �빮�ڷ� ��ȯ����
print(note.capitalize())
#a�� f�� �ٲ���
print(note.replace("a" , "f"))
