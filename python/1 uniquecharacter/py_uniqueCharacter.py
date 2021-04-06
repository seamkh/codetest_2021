def isUniqueChars(s):
    #ascii
    if(len(s) > 256):
        return False
    
    char_set = [False]*256

    for i in range(0,len(s)):
            #string to ascii
            val = ord(s[i])
            print(s[i])
            print(val)
            print(char_set[i])
            if(char_set[val]):
                print('contain same character')
                return False;
            
            char_set[val] = True

    print('not contain same character')
    return True

#test function
isUniqueChars('hello')
