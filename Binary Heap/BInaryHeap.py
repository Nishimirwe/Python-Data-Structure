class MinHeap:
    def __init__(self,capacity):
        self.capacity=capacity
        self.Heap=[0]*self.capacity
        self.length=0

    def isFull(self):
        if self.length==self.capacity:
            return True
        return False

    def isEmpty(self):
        if self.length==0:
            return True
        return False

    def addValue(self,value):
        if self.isFull():
            print("Heap is full, cannot hold", value)
        else:
            self.Heap[self.length]=value
            if self.length>0:
                index=self.length
                while self.Heap[index]<self.Heap[(index-1)//2]:
                    self.Heap[index],self.Heap[(index-1)//2]=(self.Heap[(index-1)//2],self.Heap[index])
                    index=(index-1)//2
            self.length+=1

    def Heapify(self, index):
        left=(2*index)+1
        right=(2*index)+2
        if left>self.length-1 or right>self.length-1:
            return
        while (self.Heap[left]<self.Heap[index] or self.Heap[right]<self.Heap[index]):
            if self.Heap[left]<=self.Heap[right]:
                self.Heap[index],self.Heap[left]=(self.Heap[left],self.Heap[index])
                self.Heapify(left)
            else:
                self.Heap[index],self.Heap[right]=(self.Heap[right],self.Heap[index])
                self.Heapify(right)

    def extractMin(self):
        if self.isEmpty():
            return "Empty Heap", -1
        x=self.Heap[0]
        self.Heap[0],self.Heap[self.length-1]=(self.Heap[self.length-1],self.Heap[0])
        self.Heap[self.length-1]=0
        print(self.Heapify(0))
        self.length-=1
        return x

    def show(self):
        if self.isEmpty():
            print("Empty")
        else:
            for i in self.Heap:
                if i !=0:
                    print(i,"::",end='')
            print()
            print("Size: ",self.length)

mh=MinHeap(10)
mh.addValue(10)
mh.addValue(20)
mh.addValue(5)
mh.addValue(2)
mh.addValue(3)
mh.addValue(15)
mh.addValue(17)
mh.show()
print(mh.extractMin())
mh.show()


