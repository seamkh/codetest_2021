# -*- coding: cp949 -*-
from linkedList import *
#header�� ���� �Ұ�, ������ ��常 ������ �� ���� 
def deleteNode(n):
    if n is None or n.next is None :
        return False
    #������忡 ����, next�� ��������� next�� ��ü 
    next = n.next
    n.data = next.data
    n.next = next.next
    return True

#test
a = LinkedList()
a.insert('a')
a.insert('b')
a.insert('c')
a.insert('d')
a.insert('e')
a.printList()
deleteNode(a.head.next)
#������ �μ� ó�� �ʿ�
a.printList()
