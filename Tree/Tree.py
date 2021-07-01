class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class QNode:
    def __init__(self, value):
        self.data=value
        self.Next=None

class stack: # stack is useful to traverse Tree using loops
    def __init__(self):
        self.top=None
        self.length=0

    def isEmpty(self):
        if not self.top:
            return True
        return False

    def push(self, value):
        node=QNode(value)
        if self.isEmpty():
            self.top=node
            self.length+=1
        else:
            node.Next=self.top
            self.top=node
            self.length+=1

    def pop(self):
        if self.isEmpty():
            print("Empty ",end='')
            return -1
        else:
            x=self.top.data.data
            self.top=self.top.Next
            self.length-=1
            return x

    def Size(self):
        return self.length

    def getTop(self):
        if self.isEmpty():
            print("Empty ",end='')
            return -1
        return self.top.data

    def show(self):
        if self.isEmpty():
            print("Empty")
        else:
            nav=self.top
            while nav:
                print(nav.data.data,"::", end='')
                nav=nav.Next
            print()
            print("Size: ",self.length)
#End of stack


class queue: # Queue is very useful in creating a binary Tree in complete manner 
    def __init__(self):
        self.front=None
        self.back=None
        self.length=0

    def isEmpty(self):
        if not self.front:
            return True
        return False

    def push(self,value):
        node=QNode(value)
        if self.isEmpty():
            self.back=node
            self.front=node
            self.length+=1
        else:
            self.back.Next=node
            self.back=node
            self.length+=1

    def pop(self):
        if self.isEmpty():
            return "Empty Stack", -1
        elif self.front==self.back:
            x=self.front.data.data
            self.front=self.back=None
            self.length-=1
            return x
        else:
            x=self.front.data.data
            self.front=self.front.Next
            self.length-=1
            return x
    
    def getFront(self):
        if self.front:
            return self.front
        return "Empty Queue" -1

    def show(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            nav=self.front
            while nav:
                print(nav.data.data,"::",end='')
                nav=nav.Next
            print()
            print("Size: ",self.length)
#End of Queue

class Tree:
    def __init__(self):
        self.root=None
        self.length=0
        self.que=queue()

    def addLeaf(self,value):
        node=Node(value)
        if not self.root:
            self.root=node
            self.que.push(self.root)
            self.length+=1
        elif not self.que.getFront().data.left:
            t=self.que.getFront().data
            t.left=node
            self.que.push(node)
            self.length+=1
        elif not self.que.getFront().data.right:
            t=self.que.getFront().data
            t.right=node
            self.que.push(node)
            self.que.pop()
            self.length+=1
        else: 
            pass

    def showQueue(self):
        self.que.show()

    #Traversing a Tree
    def preOrderLoop(self):
        stk=stack()
        stk.push(self.root) #push root in the stack
        while not stk.isEmpty() and stk.getTop(): # while stack is not empty and tree has the root
            t=stk.getTop() #get top of stack
            if not t.left and not t.right: #if top element has no left and right (it is the leaf), Remove it in the stack and print it
                pdata=t.data
                stk.pop()
                print(pdata,"::",end='')
            elif t.left and not t.right: #if top elmt has only left child, pop that element and push its left child
                pdata=t.data
                stk.pop()
                stk.push(t.left)
                print(pdata,"::",end='')
            elif t.right and not t.left: #if top elmt has only right child, pop that element and push its right child
                pdata=t.data
                stk.pop()
                stk.push(t.right)
                print(pdata,"::",end='')
            else: #if top elmt has all left and right children, pop it and add all children from right to left
                pdata=t.data
                stk.pop()
                stk.push(t.right)
                stk.push(t.left)
                print(pdata,"::",end='')
        else:
            print("End")
        print()

    def preOrder(self, r): # preorder using recursion
        if r:
            print(r.data,"::",end='')
            self.preOrder(r.left)
            self.preOrder(r.right)

    def inOrderLoop(self):
        print("")
    
    def inOrder(self, r): #in Order using recursion
        if r:
            self.inOrder(r.left)
            print(r.data,"::",end='')
            self.inOrder(r.right)

    def postOrder(self, r): #PostOrder traversal using recursion
        if r:
            self.postOrder(r.left)
            self.postOrder(r.right)
            print(r.data,"::",end='')

    def levelOrder(self): #Level Order using Queue
        q=queue()
        q.push(self.root)
        while not q.isEmpty() and q.getFront():
            t=q.getFront().data
            if t.left and t.right:
                q.push(t.left)
                q.push(t.right)
                print(t.data,"::",end='')
                q.pop()
            elif t.left and not t.right:
                q.push(t.left)
                print(t.data,"::",end='')
                q.pop()
            elif not t.left and t.right:
                q.push(t.right)
                print(t.data,"::",end='')
                q.pop()
            else:
                print(t.data,"::",end='')
                q.pop()
        else:
            print("End")
        print()


tr=Tree()
tr.addLeaf(1)
tr.addLeaf(2)
tr.addLeaf(3)
tr.addLeaf(4)
tr.addLeaf(5)
tr.addLeaf(6)
tr.addLeaf(7)
tr.addLeaf(8)
tr.addLeaf(9)
tr.addLeaf(10)
tr.showQueue()
tr.preOrder(tr.root)
print()
print("Below is pre order with loop")
tr.preOrderLoop()

print("In order")
tr.inOrder(tr.root)

print()
print("PostOrder")
tr.postOrder(tr.root)
print()
print()
print("Level Order: ")
tr.levelOrder()

