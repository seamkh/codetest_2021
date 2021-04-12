# -*- coding: cp949 -*-
def isRotation(s1,s2):
    length = len(s1)
    returnValue = False
    #s1과 s2의 길이가 같고, 0 보다 큰지 확인
    if length == len(s2) and length > 0 :
        # s1과 s1을 연결해 새 문자열 생성
        s1s1 = s1 + s1
        
        if s1s1.find(s2):
            returnValue = True
        else :
            returnValue = False
    print(returnValue)
    return returnValue



#test
isRotation('abcd','cdab')
