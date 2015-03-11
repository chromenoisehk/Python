area = 0
height = 10
width = 20
area = width * height /2
#print("the area of the triangle would be " + area)
print("the area of the triangle would be %.2f" % area)
#%f는 부동 소수점 수 : 일반적으로 소수점 아래 자리의 값을 담음
#%d는 10진수 보통 전체 정수와 소수점 아래 정수가 없는 값을 담음
print("I have %d cats" % 6) # 기본
print("I have %3d cats" % 6) #문자가 들어갈 공간이 3글자.
print("I have %03d cats" % 6) # %??d -> ??=자연수의 자릿수
print("I have %f cats" % 6)
#%.?f -> ?=소숫점의 자릿수
print("I have %.2f cats" % 6)
print("I have %.4f cats" % 6)

print("I have {0:d} cats".format(6))
print("I have {1:d} cats".format(6, 4))

print("Here are Three numbers! first- {0:d}, second- {1:03d}, three is {2:f}!".format(5,7,1))
