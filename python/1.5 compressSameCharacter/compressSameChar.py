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

#test
compressBad('aaaabbbccccc')
