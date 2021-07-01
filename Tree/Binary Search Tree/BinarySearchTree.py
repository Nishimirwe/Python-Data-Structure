#Binary Search Tree(BST) is a tree with additional; properties
# In BST, all left element are lesser than or equal to root node
# And right elements are all greater than root node

#When you display InOreder Traversal of BST, it is sorted
class QNode:
    def __init__(self, value):
        self.data=value
        self.Next=None

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

class Node:
    def __init__(self, value):
        self.data=value
        self.left=None
        self.right=None

class BSTTree:
    def __init__(self):
        self.root=None
        self.length=0

    def isEmpty(self):
        if not self.root:
            return True
        return False

    def push(self, value): #While pushing, place a new node at the right position following BST protocol
        node=Node(value)
        if self.isEmpty():
            self.root=node
            self.length+=1
        else:
            nav=self.root
            while 1:
                if node.data>nav.data: #If new value is greater than root, check right of the tree
                    if nav.right: #If no right, save that as right
                        print("Move right of ", nav.data)
                        nav=nav.right
                    else: #if right is there, we move to right 
                        print("save right of ",nav.data)
                        nav.right=node
                        self.length+=1
                        print("------------------------------")
                        break
                else: #if new node <= root, check left side
                    if nav.left: # Again, if no left, save new node as the left child
                        print("Move left of ",nav.data)
                        nav=nav.left
                    else: #if left is there, move left
                        print("save left of ",nav.data)
                        nav.left=node
                        self.length+=1
                        print("------------------------------")
                        break

    def levelOrder(self): #Traversing using Level order traversal algorithm
        if self.isEmpty():
            print("Empty")
        else:
            nav=self.root
            q=queue()
            q.push(nav)
            while not q.isEmpty() and q.getFront():
                t=q.getFront().data
                if t.left and t.right:
                    q.push(t.left)
                    q.push(t.right)
                    q.pop()
                    print(t.data,"::",end='')
                elif t.left and not t.right:
                    q.push(t.left)
                    q.pop()
                    print(t.data,"::",end='')
                elif not t.left and t.right:
                    q.push(t.right)
                    q.pop()
                    print(t.data,"::",end='')
                else:
                    q.pop()
                    print(t.data,"::",end='')
            print()

    #Search a value in BST
    def search(self,value):
        if self.isEmpty():
            return "Empty"
        else:
            nav=self.root
            while nav: #while we have not yet reached the leaf
                if nav.data==value: #if we reach the value we are looking for
                    return True,"Found"
                elif value<nav.data: #If value < current node, move left
                    nav=nav.left
                else: #else means value is greater, we move right
                    nav=nav.right
            return False,"Not Found"

    def search1(self,r,value): #Search using recursion
        if r:
            if r.data==value:
                print(True,"Found")
            elif value<r.data:
                self.search1(r.left,value)
            else:
                self.search1(r.right,value)
        else:
            print(False,"Not Found")

BST=BSTTree()
BST.push(70)
BST.push(50)
BST.push(60)
BST.push(30)
BST.push(90)
BST.push(80)
BST.push(20)
BST.push(71)
BST.push(85)
BST.push(100)
BST.levelOrder()
print("Searching")
print(BST.search(50))
BST.search1(BST.root,85)


