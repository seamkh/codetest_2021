# -*- coding: cp949 -*-
def compressBad(s):
    mystr = ''
    last = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] == last:
            count +=1
        else :
            mystr += last + "" + (str)(count)
            last = s[i]
            count = 1
    returnValue = mystr + last + (str)(count) 
    print(returnValue)
    return returnValue


#다른 방법 
def compressAlternate(s):
    #압축결과가 원래 문자열보다 길어지는지
    size = countCompression(s)
    print(size)
    if(size >= len(s)):
        return s

    array = ['']*size
    index = 0
    last = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] == last :
            count +=1
        else :
            index = setChar(s,array,last,index,count)
            last = s[i]
            count = 1
    index = setChar(s,array,last,index,count)
    returnValue = ''.join(array)
    print(returnValue)
    return returnValue

def setChar(s,array,c,index ,count):
    array[index] = c
    index +=1

    cnt = list(str(count))
    for i in range(len(cnt)):
        array[index] = cnt[i]
        index+=1

    return index
     
def countCompression(s):
    last = s[0]
    size = 0
    count = 1
    for i in range(1, len(s)):
        if s[i] == last:
            count+=1
        else :
            last = s[i]
            size += 1 + len(str(count))
            count = 0

    size += 1 + len(str(count))

    return size



#test
compressBad('aaaabbbccccc')

compressAlternate('aaaabbbddd')
