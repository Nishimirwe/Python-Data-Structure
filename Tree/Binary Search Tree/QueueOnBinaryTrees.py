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