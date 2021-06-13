class Node:
    def __init__(self, value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self,node):
        self.head=node
        self.tail=node
        self.length=1
    def addNode(self,node):
        self.tail.next=node
        self.tail=node
        self.length+=1
    def display(self):
        if self.head is not None:
            nav=self.head
            while nav is not None:
                print(nav.data,"->",end='')
                nav=nav.next
            print()
    def size(self):
        return self.length

    def addFirst(self, node):
        next=self.head
        self.head=node
        node.next=next
        self.length+=1
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
    def searchIn(self, value):
        nav=self.head
        while nav is not None:
            if nav.data==value:
                return value,"has been found"
            nav=nav.next
        return value,"is not in the linked list"

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
link=LinkedList(n1)
link.addNode(n2)
link.addNode(n3)
link.addNode(n4)
link.addNodeAt(n5,2)
link.addFirst(Node(12))
link.display()
print(link.searchIn(12))