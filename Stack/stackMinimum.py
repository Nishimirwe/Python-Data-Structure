#The question is to use stack and push many value as you wish
# but while poping, We want to only pop the minimu value of all elements remaining in the stack
# And Pop and Push method should all be O(1) tome complexity.
class Node:
    def __init__(self,value): #I use a stack of Linked list
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.Head=None
        self.size=0
        
    def isEmpty(self): #check if the stack is empty or not
        if self.Head==None:
            return True
        return False

    def popMin(self): # Pop min value in the stack
        if not self.isEmpty():
            t=self.Head
            self.Head=self.Head.next #always I want that the Head will be the Min value in the stack.
            self.size-=1
            x=t.data
            return t.data
        else:
            return "Stack is empty", -1

    def push(self, value): #Time to push
        node=Node(value)
        if self.Head==None: #In case this is the first Node to be added in the stack
            self.Head=node
            self.size+=1
        elif self.Head.data < value: #In case new value > than Head(Min element of existing values).
            # What we do, We do not have to store that value, No, we have to double the Min value from Head.
            # for example if I had 2->3->6, new value is 10: I make 2->2->3->6
            t=Node(self.Head.data)
            t.next=self.Head
            self.Head=t
            self.size+=1
        elif self.Head.data > value: #in case the new value is smaller than the existing smaller number.
            #Add it as new head
            node.next=self.Head
            self.Head=node
            self.size+=1

    def display(self):
        if self.isEmpty():
            print("Empty satack")
        else:
            nv=self.Head
            while nv:
                print(nv.data,"::",end=' ')
                nv=nv.next
            print()
            print("Size: ",self.size)

stk=Stack()
stk.push(10)
stk.push(20)
stk.push(5)
stk.push(25)
stk.push(53)
stk.push(50)
stk.push(3)
print(stk.popMin())
print(stk.popMin())
print(stk.popMin())
print(stk.popMin())
print(stk.popMin())
print(stk.popMin())
stk.display()
        

