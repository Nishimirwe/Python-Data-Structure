from random import *

class stack:
    def __init__(self):
        self.l=list()
        self.length=0
    
    #Add Node to stack
    def push(self,node):
        self.l.append(node)
        self.length+=1
    #pop
    def pop(self):
        self.length-=1
        node=self.l[self.length]
        self.l[self.length]=None
        return node

    #size
    def size(self):
        return self.length

    #display
    def display(self):
        for i in range(self.length):
            print(self.l[i].data,"::",end='')
        print()
        print("Size: ",self.length)

class Node:
    def __init__(self,value):
        self.Prev=None
        self.data=value
        self.Next=None

class CDLinkedList:
    def __init__(self):
        self.Head=None
        self.Tail=None
        self.length=0
    #create a linked list
    def create(self,value):
        if self.Head:
            return "The linked list is already to life", -1
        else:
            node=Node(value)
            self.Head=node
            self.Tail=node
            self.Head.Prev=self.Tail
            self.Tail.Next=self.Head
            self.length+=1

    #generate random numbers
    def randomFill(self,n,mi,ma):
        for i in range(n):
            self.addLast(randint(mi,ma))

    #add First Node
    def addFirst(self,value):
        if not self.Head:
            self.create(value)
        else:
            node=Node(value)
            node.Next=self.Head
            node.Prev=self.Head.Prev
            self.Head.Prev.Next=node
            self.Head=node
            self.length+=1
       
    #Add last Node
    def addLast(self,value):
        if not self.Head:
            self.create(value)
        else:
            node=Node(value)
            node.Prev=self.Tail
            self.Tail.Next=node
            self.Head.Prev=node
            node.Next=self.Head
            self.Tail=node
            self.length+=1

    #Delete First
    def deleteFirst(self):
        if not self.Head:
            return "Empty list"
        elif self.Head==self.Tail:
            self.Head.Next=None
            x=self.Head.data
            self.Tail.Prev=None
            self.length-=1
            return x
        else:
            x=self.Head.data
            self.Tail.Next=self.Head.Next
            self.Head.Next.Prev=self.Tail
            self.Head=self.Head.Next
            self.length-=1
            return x

    #Delete Last Node
    def deleteLast(self):
        if not self.Head:
            return "Empty list"
        elif self.Head==self.Tail:
            self.Head.Next=None
            x=self.Head.data
            self.Tail.Prev=None
            self.length-=1
            return x
        else:
            x=self.Tail.data
            self.Tail.Prev.Next=self.Head
            self.Head.Prev=self.Tail.Prev
            self.Tail=self.Tail.Prev
            self.length-=1
            return x

    #display a Linked List
    def __(self):
        if not self.Head:
            print("Empty List")
        else:
            nav=self.Head
            i=0
            while 1:
                if i==0:
                    i+=1
                print(nav.data,"->",end='')
                nav=nav.Next
                if nav==self.Head:
                    break;
        print()
        print("Size: ",self.length," Head: ",self.Head.data," Tail: ",self.Tail.data)

    #remove duplicates
    def removeDups(self):
        if not self.Head:
            print("No list")
        elif self.Head==self.Tail:
            print("One element is ther, so, no dups")
        else:
            nav=self.Head
            li=list()
            while True:
                if nav.data not in li:
                    li.append(nav.data)
                else:
                    nav.Prev.Next=nav.Next
                    if nav.Next==self.Head:
                        nav.Prev.Next=self.Head
                        self.Head.Prev=nav.Prev
                        self.Tail=self.Tail.Prev
                    else:
                        nav.Next.Prev=nav.Prev
                    self.length-=1
                nav=nav.Next
                if nav==self.Head:
                    break
    
    #return k th item
    def returnkth(self,k):
        if k>self.length:
            return "K is larger", -1
        nav=self.Head
        st=stack()
        while True:
            st.push(nav)
            nav=nav.Next
            if nav==self.Head:
                break
        i=1
        if st.size()==0:
            return "This list was empty"
        else:
            res=None
            while st.length!=0 and i<=k:
                res=st.pop()
                i+=1
            if res!=-1010101:
                return res.data
            return "K is larger",res

    #return kth 1
    def returnkth1(self,k):
        nav=self.Head
        i=0
        while 1:
            nav=nav.Next
            i+=1
            if nav==self.Head:
                break
        if k>i:
            return "K is larger", -1
        j=i-(k-1)
        i=0
        nav=self.Head
        while 1:
            i+=1
            if i==j:
                return nav.data
            nav=nav.Next

cdl=CDLinkedList()
cdl.randomFill(20,1,30)
cdl.__()
cdl.removeDups()
cdl.__()
print("-------------------------------------------------------------")
print(cdl.returnkth(30))
print(cdl.returnkth1(30))
