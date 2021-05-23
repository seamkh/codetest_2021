from dlist import DList
if __name__ == '__main__':
    s = DList()
    s.insert_after(s.head,'apple')
    s.insert_before(s.tail, 'orange')
    s.insert_before(s.tail,'cherry')
    s.insert_after(s.head.next,'pear')
    s.print_list()
    print('마지막 노드 삭제 후 : \t', end = '')
    s.delete(s.tail.prev)
    s.print_list()
    print('맨 끝에 포토 삽읍 후 : \t', end = '')
    s.insert_before(s.tail,'grape')
    s.print_list()
    print('첫 노드 삭제 후 : \t', end = '')
    s.delete(s.head.next)
    s.print_list()
    print('첫 노드 삭제 후 : \t', end = '')
    s.delete(s.head.next)
    s.print_list()
    print('첫 노드 삭제 후 : \t', end = '')
    s.delete(s.head.next)
    s.print_list()
    print('첫 노드 삭제 후: \t', end = '')
    s.delete(s.head.next)
    s.print_list()
    