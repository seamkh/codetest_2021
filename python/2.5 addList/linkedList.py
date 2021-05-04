# -*- coding: cp949 -*-
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        HeadNode = Node("HEAD")
        self.head = HeadNode
        self.tail = HeadNode
        self.NumOfData = 0
        
    def insert(self,data):
        insertNode = Node(data)
        self.tail.next = insertNode
        self.tail = insertNode
        self.NumOfData += 1
        
    def delete(self):
        if self.NumOfData == 0:
            print("List is empty!")
            return False
        elif self.NumOfData == 1:
            delete_node = self.head.next
            self.head.next = None
            self.tail = self.head
            self.NumOfData -= 1
            print("����Ʈ����",delete_node.data,"�����͸� �����Ͽ����ϴ�.")
            return delete_node.data
        else:
            delete_node = self.head.next
            self.head.next = self.head.next.next
            self.NumOfData -= 1
            print("����Ʈ���� ",delete_node.data,"�����͸� �����Ͽ����ϴ�.")
            return delete_node.data
            
    def search(self,data):
        check = self.head
        for i in range(self.NumOfData):
            if check.next.data == data:
                print(data,"�����ʹ�",i+1,"��°�� �ֽ��ϴ�.")
                return None
            check = check.next
        print(data,"�����ʹ� ����Ʈ�� �����ϴ�.")
        return None
        
    def listNum(self):
        print("���� ����Ʈ����",self.NumOfData,"���� ��Ұ� �ֽ��ϴ�.")
        return self.NumOfData
    
    def printList(self):
        current = self.head
        if self.NumOfData == 0:
            print("List is empty!")
            return None
        print("HEAD::")
        for i in range(self.NumOfData-1):
            print(current.next.data,"->")
            current = current.next
        print(current.next.data)

