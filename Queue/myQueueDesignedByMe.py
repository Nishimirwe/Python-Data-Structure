class Queue:
    def __init__(self):
        self.li=list()
        self.s=-1
        self.min=0
        self.reset=-1010

    #def isEmpty
    def isEmpty(self):
        if self.min > self.s:
            return True
        return False

    #def push
    def push(self,value):
        self.s+=1
        self.li.append(value)

    #def pop()
    def pop(self):
        if not self.isEmpty():
            x=self.li[self.min]
            self.li[self.min]=self.reset
            self.min+=1
            return x
        return "Empty List", -1

    #def front
    def front(self):
        if not self.isEmpty():
            return self.li[self.min]
        return "Empty List", -1
    
    #back element
    def back(self):
        if not self.isEmpty():
            return self.li[self.s]
        return "Empty List", -1

    #diplay()
    def display(self):
        if not self.isEmpty():
            for i in range(self.min,self.s+1):
                print(self.li[i],"::",end='')
            print()
            print("Size: ",self.s+1-self.min)
        else:
            print("Empty List")
    #Destroy
    def destroy(self):
        self.min=0
        self.s=-1
        self.li.clear()

q=Queue()
q.push(12)
q.push(15)
q.push(20)
q.push(25)
q.push(30)
q.display()
q.destroy()
q.push(30)
q.push(25)
print("Pop: ",q.pop()," Front: ",q.front()," Back: ",q.back())
q.display()
