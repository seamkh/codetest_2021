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

            #위쪽을 저장 
            top = mat[first][i]
            #왼쪽 -> 위쪽
            mat[first][i] = mat[last - offset][first]
            #아래쪽->왼쪽
            mat[last-offset][first] = mat[last][last-offset]
            #오른쪽->아래
            mat[last][last-offset] = mat[i][last]
            mat[i][last] = top
            

print(sampleMat)
rotateMat(sampleMat,3)
print('after rotate')
print(sampleMat)
rotateMat(sampleMat,3)
print('after rotate again')
print(sampleMat)
