from linkedList import *

def addList(l1, l2, carrry):
    if(l1 is None and l2 is None and carry is 0):
        return None

    result = Node(carry)

    value = carry

    if(l1 is not None):
        value += l2.data

    result.data = value%10

    if(l1 is not None or l2 is not None or value >=10):
        more = addLists(None if l1 is None else l1.next,None if l2 is None else l2.text,
                        1 if value >= 10 else 0)
        result.setNext(more)

    return result
    


