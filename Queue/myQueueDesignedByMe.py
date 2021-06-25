class Queue:
    def __init__(self):
        self.li=list()
        self.s=-1
        self.min=0
        self.reset=-1010

    #def push
    def push(self,value):
        self.s+=1
        self.li.append(value)

    #def pop()
    def pop(self):
        x=self.li[min]
        self.li[min]=self.reset
        self.min+=1
        self.s-=1
        return x

    #def front
    def front(self):
        return self.li[min]
    
    #back element
    def back(self):
        return self.li[s]

    #diplay()
    def display(self):
        for i in range(self.min,self.s+1):
            print(self.li[i],"::",end='')
        print()
        print("Size: ",self.s+1)

q=Queue()
q.push(12)
q.push(15)
q.push(20)
q.push(25)
q.push(30)
q.display()
