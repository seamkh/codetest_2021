from linkedList import *

def nthToLast(head,k):
    if head is None :
        return 0

    i = nthToLast(head.next,k) + 1
    if i == k :
        print(head.data)
    return i

a = LinkedList()
a.insert('a')
a.insert('b')
a.insert('c')
a.insert('d')
a.insert('e')
a.printList()
nthToLast(a.head,3)

