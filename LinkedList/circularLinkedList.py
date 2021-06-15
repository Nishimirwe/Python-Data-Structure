class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def __init__(self,value):
        self.data=value
class doubleLinkedList:
    #Constructor
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    #Adding a new node in a list
    def addLast(self, node):
        if self.head is None:
            self.head=node
            self.tail=node
            node.next=self.head
            self.length+=1
        else:
            nav=self.head
            while nav is not None:
                if nav.next==self.head:
                    break
                nav=nav.next
            nav.next=node
            node.next=self.head
            self.tail=node
            self.length+=1

    #insert Node at the beginning of Linked List
    def addFirst(self, node):
        if self.head is None:
            self.head=node
            self.tail=node
            node.next=node
            self.length+=1
        else:
            t=self.head #Current First Node
            tt=self.tail #Last Node
            node.next=t #step 1
            self.head=node #step 2
            tt.next=self.head
            self.length+=1

    # inser a new node at a specific location
    def insert(self, node, location):
        if location <1 or location > self.length:
            print("This index is invalid")
        elif self.head is None or location == 1:
            self.addFirst(node)
        elif location==self.length:
            self.addLast(node)
        else:
            i=1
            nav=self.head
            while i<location-1:
                nav=nav.next
                i+=1
            t=nav.next
            nav.next=node
            node.next=t
            self.length+=1
  
    #Displaying linked list
    def display(self):
        if self.head is None:
            print("The linked list is Empty")
        else:
            nav=self.head
            while nav is not None:
                print(nav.data,"->",end='')
                if nav.next==self.head:
                    break
                nav=nav.next
            print()
        print("Head: ",self.getHead()," Tail: ",self.getTail()," and length: ",self.size())
    
    #Return next of a node
    def getNextOf(self, node):
        if self.head is None:
            return "The linked list is empty"
        return node.next.data

    #return the head of Linked List
    def getHead(self):
        if self.head is None:
            return "The linked list is empty"
        return self.head.data

    #return the tail of Linked List
    def getTail(self):
        if self.head is None:
            return "The linked list is empty"
        return self.tail.data
    
    #Return the size of Linked List
    def size(self):
        return self.length

    #Search Node in a linked list
    def search(self, value):
        if self.head is None:
            return "The list is empty"
        else:
            nav=self.head
            while nav is not None:
                if nav.data==value:
                    return True,value," is present in the list"
                elif nav==self.tail:
                    return False, value," is absent in the list"
                else:
                    pass
                nav=nav.next
    #delete First Node of the linked list
    def deleteFirst(self):
        if self.head is None:
            print("The list has no node")
        elif self.head==self.tail:
            self.head.next=None
            self.head=None
            self.tail=None

            self.length-=1
        else:
            newHead=self.head.next
            self.head=newHead
            self.tail.next=self.head  
            self.length-=1
      
    #Delete Last Node From the Linked List
    def deleteLast(self):
        if self.head is None:
            print("The linked List is Empty")
        elif self.head==self.tail:
            self.head.next=None
            self.head=None
            self.tail=None
            self.length-=1
        else:
            nav=self.head
            while nav.next!=self.tail:
                nav=nav.next
            nav.next=self.head
            self.tail=nav
            self.length-=1

    #Delete Node at a sepcific position
    def deleteAt(self, location):
        if location>self.length or location<1:
            print("No, the location is invalid, it varies from ",1," to ",self.length)
        elif location==1:
            self.deleteFirst()
        elif self.head==self.tail:
            self.deleteLast()
        elif location==self.length:
            self.deleteLast()
        elif self.head is not None:
            i=1
            nav=self.head
            while i<location-1:
                nav=nav.next
                i+=1
            nav.next=nav.next.next
        else:
            print("Empty Linked list")

    #Delete entire Linked list
    def deleteEntire(self):
        self.head.next=None
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
            
dl=doubleLinkedList()
n1=Node(10)
n2=Node(90)
n3=Node(130)
n4=Node(5)
n5=Node(7)
n6=Node(200)
dl.addLast(n1)
dl.addLast(n2)
dl.addLast(n3)
dl.addLast(n4)
dl.addLast(n5)
dl.display()
