from abc import ABC,abstractmethod
class Item:
    def __init__(self,itemName=None,price=None,next = None):
        self.itemName = itemName
        self.price = price
        self.next = next
class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self,itemName,price):
        new_node = Item(itemName,price)
        if(self.head==None):
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    def printToEnd(self):
        curr = self.head
        while(curr!=None):
            print(curr.itemName, curr.price)
            curr = curr.next

    def sorted_insert(self,val):
        new_node = Item(val)
        if(self.head == None):
            self.head = new_node
            return self.head
        if(val[0]<self.head.data_1[0]):
            self.head = self.insertAtBegin(val)
            return self.head
        curr = self.head
        if(curr.next==None):
            if(curr.data_1[0]<val[0]):
                self.head = self.insertAtEnd(val)
            else:
                self.head = self.insertAtBegin(val)
            return self.head
        while(curr.next!=None and curr.next.data_1[0]<val[0]):
            curr = curr.next
            print(curr.data_1[0])
        new_node.next = curr.next
        curr.next = new_node
        return self.head
            

    def insertAtEnd(self,itemName,price):
        new_node = Item(itemName,price)
        if(self.head==None):
            self.head = new_node
            return self.head
        curr = self.head
        while(curr.next!=None):
            curr = curr.next
        curr.next = new_node
        return self.head
    
    
    def deleteAtHead(self):
        self.head = self.head.next
        return self.head
    
    def deleteEnd(self):
        curr = self.head
        while(curr.next.next!=None):
            curr = curr.next
        curr.next = None
        return self.head
    
    def divideList(self,head,div):
        curr = head
        while(curr!=None and div>1):
            curr = curr.next
            div-=1
        temp = curr
        if(curr):
            curr = curr.next
            temp.next = None
        return head,curr
    
    def sizeofLL(self,head):
        if(head==None):
            return 0
        if(head.next==None):
            return 1
        curr = head
        size = 0
        while(curr):
            curr = curr.next
            size+=1
        return size

    def mergeSort(self,head):
        if(self.sizeofLL(head)<=1):
            return head
        left_list = head
        right_list = head
        mid = self.sizeofLL(head)//2
        left_list,right_list = self.divideList(head,mid)
        # printToEnd(left_list)
        # print('----------')
        # printToEnd(right_list)
        left_list = self.mergeSort(left_list)
        right_list = self.mergeSort(right_list)

        return self.mergeLL(left_list,right_list)

    def mergeLL(self,head1,head2):
        # printToEnd(head1)
        # printToEnd(head2)
        mergeListHead = Item()
        resHead = mergeListHead
        while(head1 and head2):

            if(head1.data<head2.data):
                mergeListHead.next = head1
                head1 = head1.next
            else:
                mergeListHead.next = head2
                head2 = head2.next

            mergeListHead = mergeListHead.next
            
            if(head1==None):
                mergeListHead.next = head2
                head2 = head2.next
            elif(head2==None):
                mergeListHead.next = head1
                head1 = head1.next
            
        
        return resHead.next


List = LinkedList()
# item_1 = Item(['Pizza',345])
# item_2 = Item(['Cake',420])
head = List.insertAtEnd('Pizza',350)
# print(List.head.itemName)
head = List.insertAtEnd('cake',420)
# print(List.head.next.itemName)
List.printToEnd()

