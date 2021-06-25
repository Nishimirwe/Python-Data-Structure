class circularQueue:
    def __init__(self,c):
        self.capacity=c
        self.li=[None]*c
        self.S=0
        self.start=0
        self.end=-1

    #isEmpty
    def isEmpty(self):
        if self.S==0 or self.end==-1:
            return True
        return False

    #is full
    def isFull(self):
        if self.S<self.capacity:
            return False
        return True

    #enqueueu
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full to not afford new data", value)
            return -1
        self.S+=1
        if self.end+1 == self.capacity:
            print("Case")
            self.end=0
        else:
            self.end+=1
        self.li[self.end]=value

    def dequeue(self):
        if self.isEmpty():
            return "Already Empty", -1
        x=self.li[self.start]
        self.li[self.start]=None
        if self.start==self.capacity-1:
            self.start=0
        else:
            self.start+=1
        self.S-=1
        return x

    #display
    def display(self):
        if not self.isEmpty():
            for i in range(self.capacity):
                if self.li[i] is not None:
                    print(self.li[i],"::",end='')
            print()
            print("Start: ",self.start, self.li[self.start],", End: ",self.end, self.li[self.end],", Size: ",self.S, ", Full: ", self.isFull(),", Empty: ",self.isEmpty())
        else:
            print("Empty")

    #delete Queue
    def delete(self):
        self.li.clear()
        self.li=[None]*self.capacity
        self.start=0
        self.end=-1

cq=circularQueue(5)
print(cq.isEmpty())
cq.enqueue(10)
cq.enqueue(15)
cq.dequeue()
cq.enqueue(20)
cq.dequeue()
cq.enqueue(30)
cq.delete()
cq.display()