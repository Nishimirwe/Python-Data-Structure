class multiStacks:
    def __init__(self, largeSize,StacksNum):
        self.largeSize=largeSize
        self.StacksNum=StacksNum
        self.larger=[0]*self.largeSize
        self.stackSize=[0]*StacksNum
        self.eachSize=largeSize//StacksNum

    def isEmpty(self,index):
        if self.stackSize[index-1]<0:
            return True
        return False

    def isFull(self, index):
        if self.stackSize[index-1]==self.eachSize:
            return True
        return False
    
    def push(self, index, value):
        if not self.isFull(index-1):
            self.larger[self.eachSize*(index-1)+self.stackSize[index-1]]=value
            self.stackSize[index-1]+=1
        else:
            print("The stack", index, "is full")

    def pop(self,index):
        if not self.isEmpty(index-1):
            x=self.larger[self.eachSize*(index-1)+self.stackSize[index-1]]
            self.larger[self.eachSize*(index-1)+self.stackSize[index-1]]=0
            self.stackSize[index-1]-=1
            return x
        else:
            print("The stack", index, "is empty")

    def top(self, index):
        if not self.isEmpty(index-1):
            return self.larger[self.eachSize*(index-1)+self.stackSize[index-1]]
        else:
            return "Stack ",index," is Empty"

    def display(self,index):
        if not self.isEmpty(index-1):
            for i in range(self.stackSize[index-1]):
                print(self.larger[self.eachSize*(index-1)+i],"::",end='')
            print()
            print("Stack ",index," has length of ",self.stackSize[index-1], "with top of ", self.larger[self.eachSize*(index-1)+self.stackSize[index-1]])
        else:
            print("Stack ",index, "is empty")

    def disp(self):
        for i in range(self.largeSize):
            print(self.larger[i],"::",end='')
        print()

mt=multiStacks(25,5)
mt.push(1,1)
mt.push(1,2)
mt.push(2,5)
mt.pop(1)
mt.display(1)