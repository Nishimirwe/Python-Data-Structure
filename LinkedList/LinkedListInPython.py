class Node:
    def __init__(self, value):
        self.data=value
        self.next=None

class LinkedList:
    #Constructor
    def __init__(self,node):
        self.head=node
        self.tail=node
        self.length=1
    #add new node
    def addNode(self,node):
        self.tail.next=node
        self.tail=node
        self.length+=1
    ##Display the linked dist
    def display(self):
        if self.head is not None:
            nav=self.head
            while nav is not None:
                print(nav.data,"->",end='')
                nav=nav.next
            print()
    # Return the size of linked list, number of nodes
    def size(self):
        return self.length
    #Add node at the beginning
    def addFirst(self, node):
        next=self.head
        self.head=node
        node.next=next
        self.length+=1
    #Add a node at the certain position
    def addNodeAt(self, node, location):
        if location<1 or location > (self.length+1):
            print("Invalid location")
        elif location > self.length:
            self.addNode(node)
        else:
            i=1
            tempNode=self.head
            while(i<location-1):
                tempNode=tempNode.next
                i+=1
            next=tempNode.next
            tempNode.next=node
            node.next=next
            self.length+=1
    #Search a value a Linked List
    def searchIn(self, value):
        nav=self.head
        while nav is not None:
            if nav.data==value:
                return value,"has been found"
            nav=nav.next
        return value,"is not in the linked list"
    #Delete First Node in the linked List
    def deleteFirst(self):
        if self.length<1:
            print("Empty is the linked list")
        elif self.length == 1:
            print("Only One element in a linked list, and the list cannot be empty")
        else:
            newHead=self.head.next
            self.head=None
            self.head=newHead
            self.length-=1
    #Return First node in the linked list
    def getHead(self):
        return self.head
    #Return Last node in the linked list
    def getTail(self):
        return self.tail
    #Delete Node at a certain position
    def deleteAt(self, location):
        if location <1 or location >self.length:
            print("No, the location is invalid, Min is ",1," and max is ",self.length)
        elif location == 1:
            self.deleteFirst()
        else:
            i=1
            nav=self.head
            while i<location-1:
                nav=nav.next
                i+=1
            toDelete=nav.next
            nav.next=nav.next.next
            toDelete=None
            self.length-=1
    #Delete Last Node in the linked list
    def deleteLast(self):
        if self.length==1:
            self.deleteFirst()
        else:
            nav=self.head
            i=1
            while i <self.length-1:
                nav=nav.next
                i+=1
            nav.next=None
            self.tail=nav
    #Delete entire Linked list
    def deleteEntire(self):
        self.head.next=None     
        self.tail=self.head
        print(self.getHead().data," ",self.getTail().data)

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
link=LinkedList(n1)
print(link.searchIn(12))
print("Deleting")
link.deleteLast()
link.display()
link.deleteEntire()
