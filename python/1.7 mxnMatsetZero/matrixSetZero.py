# -*- coding: cp949 -*-
def setZeros(mat):
    row = [False]*len(mat)
    column = [False]*len(mat[0])
    print(mat)
    #0�� ���Ұ� �ִ� ��� ���� ÷�� ���� �����Ѵ�. 
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            if mat[i][j] == 0 :
                row[i] = True
                column[j] = True
    #i���̳� j ���� 0�� ���Ҹ� ���� ��� anf[i][j]�� ���� 0���� �����
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
