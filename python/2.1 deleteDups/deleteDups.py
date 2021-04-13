# -*- coding: cp949 -*-
from linkedList import *  

def deleteDups(n):
    table = {}
    previous = None;
    while(n is not None):
        if(n.data in table):
            previous.next = n.next
        else:
            table[n.data]= True
            previous = n
        print(n.data)
        n = n.next
    
    

a = LinkedList()
a.insert('1')
a.insert('2')
a.insert('2')
a.insert('2')
a.insert('3')
deleteDups(a.head)
deleteDups(a.head)
print(a)
