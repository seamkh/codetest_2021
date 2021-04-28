from linkedList import *

def partition(node,x):
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None
    while(node is not None):
        next = node.next
        node.next = None
        if node.data < x :
            if beforeStart is None:
                beforeStart = node
                beforeEnd = beforeStart
            else :
                beforeEnd.next = node
                beforeEnd = node
        else :
            if afterStart is None:
                afterStart = node
                afterEnd = afterStart
            else :
                afterEnd.next = node
                afterEnd = node

        node = next

    if beforeStart is None :
        return afterStart

    beforeEnd.next = afterStart
    return beforeStart


a = LinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.printList()
returnValue = partition(a.head.next, 3)
print(returnValue.data)
