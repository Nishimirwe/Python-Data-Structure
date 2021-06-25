class Node:
    def __init__(self,value):
        self.data=value
        self.Next=None
        self.Prev=None

class Queue:
    def __init__(self):
        self.Head=None
        self.Tail=None
        self.S=0
    #isEmpty
    def isEmpty(self):
        if not self.Head:
            return True
        return False
    #enqueue
    def enqueue(self,value):
        node=Node(value)
        if self.isEmpty():
            self.Head=self.Tail=node
            self.S+=1
        else:
            node.Next=self.Head
            self.Head.Prev=node
            self.Head=node
            self.S+=1
    #dequeue
    def deqeueu(self):
        if self.isEmpty():
            return "Empty List",-1
        elif self.Head==self.Tail:
            x=self.Head.data
            self.Head=None
            self.Tail=None
            self.S-=1
            return x
        x=self.Tail.data
        self.Tail=self.Tail.Prev
        self.Tail.Next=None
        self.S-=1
        return x
    #peek
    def peek(self):
        if self.isEmpty():
            return "Empty List", -1
        return self.Tail.data

    #size
    def Size(self):
        return self.S

    #display()
    def display(self):
        if self.isEmpty():
            print("Empty List")
        else:
            nav=self.Head
            while nav:
                print(nav.data,"::",end='')
                nav=nav.Next
            print()
            print("Size: ",self.S," Last: ",self.Head.data," First: ",self.Tail.data)


q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()


