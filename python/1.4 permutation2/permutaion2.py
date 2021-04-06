# -*- coding: cp949 -*-
def permutation(s,t):
        if(len(s) != len(t)):
            print('길이 같지 않음')
            return False

        letters = [0]*256 #가정

        for i in range(0,len(s)):
            print('dd')
            letters[ord(s[i])]+=1

        for j in range(0,len(t)):
            print('hello')
            val = ord(t[j])
            if(letters[val]-1 < 0):
                print('다른 문자 발견')
                return False

        print('모두 같은 문자')  
        return True
            

permutation('hhh','hh0')
