area = 0
height = 10
width = 20
area = width * height /2
#print("the area of the triangle would be " + area)
print("the area of the triangle would be %.2f" % area)
#%f�� �ε� �Ҽ��� �� : �Ϲ������� �Ҽ��� �Ʒ� �ڸ��� ���� ����
#%d�� 10���� ���� ��ü ������ �Ҽ��� �Ʒ� ������ ���� ���� ����
print("I have %d cats" % 6) # �⺻
print("I have %3d cats" % 6) #���ڰ� �� ������ 3����.
print("I have %03d cats" % 6) # %??d -> ??=�ڿ����� �ڸ���
print("I have %f cats" % 6)
#%.?f -> ?=�Ҽ����� �ڸ���
print("I have %.2f cats" % 6)
print("I have %.4f cats" % 6)

print("I have {0:d} cats".format(6))
print("I have {1:d} cats".format(6, 4))

print("Here are Three numbers! first- {0:d}, second- {1:03d}, three is {2:f}!".format(5,7,1))
