# -*- coding: cp949 -*-


sampleMat = [[1,0,0],
       [0,0,0],
        [0,0,0]]

def rotateMat(mat,n):
    for layer in range(0,n/2):
        first = layer
        last = n-1-layer

        for i in range(first,last):
            offset = j = first

            #������ ���� 
            top = mat[first][i]
            #���� -> ����
            mat[first][i] = mat[last - offset][first]
            #�Ʒ���->����
            mat[last-offset][first] = mat[last][last-offset]
            #������->�Ʒ�
            mat[last][last-offset] = mat[i][last]
            mat[i][last] = top
            

print(sampleMat)
rotateMat(sampleMat,3)
print('after rotate')
print(sampleMat)
rotateMat(sampleMat,3)
print('after rotate again')
print(sampleMat)
