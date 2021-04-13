# -*- coding: cp949 -*-
from linkedList import *
#header에 접근 불가, 삭제할 노드만 접근할 수 있음 
def deleteNode(n):
    if n is None or n.next is None :
        return False
    #다음노드에 복사, next를 다음노드의 next로 대체 
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
#마지면 인수 처리 필요
a.printList()
