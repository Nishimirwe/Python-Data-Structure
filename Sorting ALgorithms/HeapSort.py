#This lgorithm uses Heap data structure and either stack or queue
#I am going to use MaxHeap, extractMax, insert Max in a stack. I time of poping, data will be sorted.
class Node:
    def __init__(self,value):
        self.data=value
        self.Next=None

class stack:
    def __init__(self):
        self.top=None
        self.length=0

    def isEmpty(self):
        if self.top:
            return False
        return True

    def push(self,value):
        node=Node(value)
        if self.isEmpty():
            self.top=node
            self.length+=1
        else:
            node.Next=self.top
            self.top=node
            self.length+=1

    def pop(self):
        if self.isEmpty():
            return -1
        x=self.top.data
        self.top=self.top.Next
        self.length-=1
        return x

    def show(self):
        if self.isEmpty():
            print("Empty Stack")
        else:
            nav=self.top
            while nav:
                print(nav.data,"::",end='')
                nav=nav.Next
            print()
            print("Size: ",self.length)


class MaxHeap:
    def __init__(self, size):
        self.size=size
        self.li=[-111]*10
        self.length=-1
        self.stk=stack()

    def ismpty(self):
        if self.length==-1:
            return True
        return False

    def isFull(self):
        if (self.length+1)==self.size:
            return True
        return False

    def parent(self,child):
        return (child-1)//2

    def LeftChild(self,parent):
        return (2*parent)+1

    def RightChild(self,parent):
        return (2*parent)+2

    def addNode(self,value):
        if self.isFull():
            print("Oops, the Heap is full")
        else:
            self.length+=1
            self.li[self.length]=value
            if(self.length!=0):
                index=self.length
                while self.li[index]>self.li[self.parent(index)]:
                    self.li[index],self.li[self.parent(index)]=(self.li[self.parent(index)],self.li[index])
                    index=self.parent(index)
                    if index==0:
                        return

    def Heapify(self,index):
        left=self.LeftChild(index)
        right=self.RightChild(index)
        if left>self.length and right>self.length:
            return
        while self.li[left]>self.li[index] or self.li[right]>self.li[index]:
            if self.li[left]>=self.li[right]:
                self.li[index],self.li[left]=(self.li[left],self.li[index])
                self.Heapify(left)
            else:
                self.li[index],self.li[right]=(self.li[right],self.li[index])
                self.Heapify(right)

    def extractMax(self):
        if self.ismpty():
            return -1
        x=self.li[0]
        self.li[0]=self.li[self.length]
        self.li[self.length]=-111
        self.length-=1
        self.Heapify(0)
        return x

    def showHeap(self):
        if self.ismpty():
            print("Oops, this is empty Heap")
        else:
            for i in range(self.length+1):
                print(self.li[i],"::",end='')
            print()
            print("Heap Size: ",self.length+1)

    def sort(self):
        for i in range(self.length+1):
            self.stk.push(self.extractMax())
        print("Let us sort our Max Heap ascendingly")
        while not self.stk.isEmpty():
            print(self.stk.pop(),"->",end='')
        print()

MH=MaxHeap(10)
MH.addNode(70)
MH.addNode(10)
MH.addNode(80)
MH.addNode(30)
MH.addNode(20)
MH.addNode(40)
MH.addNode(60)
MH.addNode(50)
MH.addNode(90)
MH.showHeap()
MH.sort()