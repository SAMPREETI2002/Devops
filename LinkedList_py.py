# create a node 
class info :
    def __init__(self,itemName,price:float) :
        self.name=itemName
        self.price=price
class Node(info) :
    def __init__(self , data , next) :
        self.data = data
        self.next = next
class LinkedList :
    def __init__(self) :
        self.head = None
        print("Initializing!")
    def append(self , element) :
        new_node = Node (element , None)
    #Adding new node
        if not self.head :
            self.head = new_node
            return
    #Add in the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    # Insert in middle
    def insertAfter(self , element , position) :
        new_node = Node(element,None)
        current = self.head
        counter=1
        while counter < position :
                current=current.next
                counter= counter + 1
        new_node.next = current.next
        current.next = new_node
    # Display          
    def display(self):
        current = self.head
        while current :
            print(current.data.name ,'-',current.data.price)
            current = current.next
    # Search for a value in linked list
    def Search(self ,element) :
        current = self.head
        while current.next != None :
            if current.data == element :
                print(f"Element found : {element}")
            current = current.next
    #Delete node with some data
    def Delete(self , data) :
        current = self.head 
        while current.next !=None :
            if current.next == data :
                current.next = current.next.next
                return
            current=current.next 
m1= info("apple",25)
m2=info("banana",10)
m3=info("kiwi",15)
m4=info("green apple",10)
l1= LinkedList()
l1.append(m1)
l1.append(m2)
l1.append(m3)
l1.append(m4)
# l1.insertAfter(10,2)
# l1.display() 
# l1.Search(10)
# l1.Delete(2)
l1.display()

    
