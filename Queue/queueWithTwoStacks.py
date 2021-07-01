class Node:
    def __init__(self,value):
        self.data=value
        self.Next=None

class stack:
    def __init__(self):
        self.top=None
        self.length=0

    def isEmpty(self):
        if not self.top:
            return True
        return False
    
    def push(self,value):
        node=Node(value)
        if not self.top:
            self.top=node
            self.length+=1
        else:
            node.Next=self.top
            self.top=node
            self.length+=1

    def Size(self):
        return self.length

    def pop(self):
        if self.isEmpty():
            return "Stack is empty", -1
        elif not self.top.Next:
            x=self.top.data
            self.top=None
            self.length-=1
            return x
        else:
            x=self.top.data
            self.top=self.top.Next
            self.length-=1
            return x
    
    def emptify(self):
        if self.isEmpty():
            print("Already empty")
        else:
            self.top=None
            self.length=0

    def show(self):
        if self.isEmpty():
            print("Empty stack")
        else:
            nav=self.top
            while nav:
                print(nav.data,"::",end='')
                nav=nav.Next
            print(" ")
            print("Size: ", self.length)

class queue:
    def __init__(self):
        self.stk1=stack()
        self.stk2=stack()
        self.use=self.stk1

    def isEmpty(self):
        if self.stk1.isEmpty() and self.stk2.isEmpty():
            return True
        return False

    def Size(self):
        return self.stk1.Size()+self.stk2.Size()
    
    def push(self,value):
        self.use.push(value)

    def pop(self):
        if self.stk2.isEmpty():
            nav=self.stk1.top
            while nav:
               self.stk2.push(nav.data)
               nav=nav.Next
            self.stk1.emptify()
        return self.stk2.pop()

    def showStacks(self):
        print("Stack 1:", end=' ')
        self.stk1.show()
        print()
        print("Stack 2:", end=' ')
        self.stk2.show()

q=queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.push(60)
print(q.pop()," ",q.pop())
q.push(70)
print(q.pop()," ",q.pop())
print(q.pop()," ",q.pop())
print(q.pop())
q.showStacks()


