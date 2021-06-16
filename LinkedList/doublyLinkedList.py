class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None

class doubleLinkedList:
    #constructor
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    #check if Linked lst is empty
    def isEmpty(self):
        if self.head is None:
            return True
        return False

    #Add a new Node
    def addNew(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
            self.length+=1
        else:
            t=self.tail
            node.previous=t
            t.next=node
            self.tail=node
            node.next=None
            self.length+=1

    #Add new Node at the beginning of Linked List
    def addFirst(self, node):
        if self.isEmpty():
            self.head=node
            self.tail=node
            self.length+=1
        else:
            t=self.head
            node.next=t
            node.previous=None
            t.previous=node
            self.head=node
            self.length+=1

    #Insert a Node at a specific position
    def insert(self, node, location):
        if location<1 or location>self.length:
            return "Index is not valid"
        elif location==1:
            self.addFirst(node)
        elif location==self.length:
            self.addNew(node)
        else:
            i=1
            nav=self.head
            while i<location-1:
                nav=nav.next
                i+=1
            nextNode=nav.next
            node.previous=nav
            nav.next=node
            node.next=nextNode
            nextNode.previous=node
            self.length+=1

    #get the previous node of a given node
    def getPreviousOf(self, node):
        if self.isEmpty():
            return "The List is empty"
        elif self.head==self.tail:
            return "There is only one Node in the list"
        elif node==self.head:
            return "This is the first Node in the List. So, No previous"
        else:
            nav=self.head
            while nav is not None:
                if nav.next==node:
                    return nav.data
                nav=nav.next
            return "Node does not exist"

    #Get the next of the given node
    def getNextOf(self, node):
        if self.isEmpty():
            return "The list is empty"
        elif self.head==self.tail:
            return "There is only one Node in the list. So, Not next is there"
        elif node==self.tail:
            return "This is the Last Node in the list. So, No node next to it"
        else:
            nav=self.tail
            while nav is not None:
                if nav.previous==node:
                    return nav.data
                nav=nav.previous
            return "The Node is not in the list"
        print()

    #Displaying my double linked list
    def display(self):
        if self.isEmpty():
            print("Our Linked List is empty")
        else:
            nav=self.head
            while nav is not None:
                print(nav.data,"<->",end='')
                nav=nav.next
            print()
            print("Head: ",self.head.data,"|| Tail: ",self.tail.data," || and Length: ",self.length)
        print("-----------------------------------------------------------")

    #Reversing a Double Linked list
    def reverse(self):
        if self.isEmpty():
            print("The list is empty")
        else:
            nav=self.tail
            while nav is not None:
                print("<-", nav.data,end='')
                nav=nav.previous
        print()
        print("-----------------------------------------")

    #Search in linked list
    def search(self, value):
        if self.isEmpty():
            return "No data in the list"
        else:
            nav=self.head
            while nav:
                if nav.data==value:
                    return value, "found"
                nav=nav.next
            return value,"is not in the list"

    #delete First Node of the list
    def deleteFirst(self):
        if self.isEmpty():
            return "No data in the list"
        elif self.head==self.tail:
            self.head=None
            self.tail=None
            self.length-=1
        else:
            self.head.next.previous=None
            self.head=self.head.next
            self.length-=1

    #delete Last Node of the list
    def deleteLast(self):
        if self.isEmpty():
            return "No data in this list"
        elif self.head==self.tail:
            self.deleteFirst()
        else:
            self.tail.previous.next=None
            self.tail=self.tail.previous
            self.length-=1

    #delete Node at a specific position
    def deleteAt(self, location):
        if self.isEmpty():
            return "No data in this list"
        elif location <0 or location>self.length:
            return "The index is not valid"
        elif location==1:
            self.deleteFirst()
        elif location==self.length:
            self.deleteLast()
        else:
            i=1
            nav=self.head
            while i<(location-1):
                nav=nav.next
                i+=1
            nextNode=nav.next.next
            nav.next.previous=None
            nav.next.next=None
            nextNode.previous=nav
            nav.next=nextNode
            self.length-=1

    #delete enetire Linked list
    def deleteEntire(self):
        if self.isEmpty():
            return "The list is already empty"
        else:
            nav=self.head
            while nav:
                nav.previous=None
                nav=nav.next
            self.head.next=None
            self.head=None
            self.tail.previous=None
            self.tail=None
            self.length=0
            return "Linked List has been deleted successfully"

dl=doubleLinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(5)
n5=Node(15)
dl.addNew(n1)
dl.addNew(n2)
dl.addNew(n3)
dl.addFirst(n4)
dl.insert(n5,3)
print(dl.deleteEntire())
dl.display()



