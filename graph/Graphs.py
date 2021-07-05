
from collections import defaultdict

class Node:
    def __init__(self,value):
        self.data=value
        self.Next=None

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


class Graph:
    def __init__(self):
        self.connection=defaultdict(list)
        self.visited=dict()
        self.length=0
        self.stk=stack()
    def add(self,v,w):
        self.connection[v].append(w)
        self.connection[w].append(v)
        self.length+=1

    def show(self):
        for i in self.connection:
            print(i,":",end='')
            for t in self.connection[i]:
                print(t,end=' ')
            print()

    def DFS(self,r): #Logic used a stack
        self.visited[r]=True
        self.stk.push(r)
        print(r,end=' ')
        for i in self.connection[self.stk.pop()]:
            if not i in self.visited.keys():
                self.stk.push(i)
                self.visited[i]=True
                self.DFS(i)

    def areTheyConnected(self): #Check if all nodes are connecteds
        for i in self.connection:
            if i not in self.visited.keys():
                return False
        return True

    def BFS(self,r): #Logic used Queue data structure
        visited=dict()
        q=Queue()
        visited[r]=True
        q.enqueue(r)
        while not q.isEmpty():
            x=q.peek()
            print(x,end=' ')
            for i in self.connection[q.deqeueu()]:
                if i not in visited.keys():
                    visited[i]=True
                    q.enqueue(i)
        print()

        

g=Graph()
g.add("A","B")
g.add("A","C")
g.add("C","E")
g.add("B","E")
g.add("E","D")
g.add("D","B")
g.add("F","E")
g.add("D","F")
g.DFS("A")
print()
print("Are They Connected together? ",g.areTheyConnected())
g.BFS("C")
