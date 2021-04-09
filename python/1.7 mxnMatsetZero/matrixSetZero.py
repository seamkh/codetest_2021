# -*- coding: cp949 -*-
def setZeros(mat):
    row = [False]*len(mat)
    column = [False]*len(mat[0])
    print(mat)
    #0인 원소가 있는 행과 열의 첨자 값을 저장한다. 
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            if mat[i][j] == 0 :
                row[i] = True
                column[j] = True
    #i행이나 j 열이 0인 원소를 갖는 경우 anf[i][j]의 값을 0으로 만든다
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            if row[i] or column[j] :
                mat[i][j] = 0

    print(mat)
    return


mat = [
        [1,1,0],
        [1,1,1],
        [1,1,1]
    ]

setZeros(mat)
