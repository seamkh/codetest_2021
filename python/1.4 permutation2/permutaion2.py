# -*- coding: cp949 -*-
def permutation(s,t):
        if(len(s) != len(t)):
            print('���� ���� ����')
            return False

        letters = [0]*256 #����

        for i in range(0,len(s)):
            print('dd')
            letters[ord(s[i])]+=1

        for j in range(0,len(t)):
            print('hello')
            val = ord(t[j])
            if(letters[val]-1 < 0):
                print('�ٸ� ���� �߰�')
                return False

        print('��� ���� ����')  
        return True
            

permutation('hhh','hh0')
