# -*- coding: cp949 -*-
def isRotation(s1,s2):
    length = len(s1)
    returnValue = False
    #s1�� s2�� ���̰� ����, 0 ���� ū�� Ȯ��
    if length == len(s2) and length > 0 :
        # s1�� s1�� ������ �� ���ڿ� ����
        s1s1 = s1 + s1
        
        if s1s1.find(s2):
            returnValue = True
        else :
            returnValue = False
    print(returnValue)
    return returnValue



#test
isRotation('abcd','cdab')
