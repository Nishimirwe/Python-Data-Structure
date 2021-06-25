class Queue:
    def __init__(self):
        self.li=list()
        self.s=0

    #def isEmpty
    def isEmpty(self):
        if self.li==[]:
            return True
        return False

    #def push
    def push(self,value):
        self.s+=1
        self.li.append(value)

    #def pop()
    def pop(self):
        if not self.isEmpty():
            self.s-=1
            return self.li.pop(0)
        return "Empty List", -1

    #def front
    def front(self):
        if not self.isEmpty():
            return self.li[0]
        return "Empty List", -1
    
    #back element
    def back(self):
        if not self.isEmpty():
            return self.li[len(self.li)-1]
        return "Empty List", -1

    #diplay()
    def display(self):
        if not self.isEmpty():
            for i in self.li:
                print(i,"::",end='')
            print()
            print("Size: ",self.s)
        else:
            print("Empty List")
    #Destroy
    def destroy(self):
        self.s=0
        self.li.clear()

q=Queue()
q.push(12)
q.push(15)
q.push(20)
q.push(25)
q.push(30)
q.push(25)
q.display()
print("Pop: ",q.pop()," Front: ",q.front()," Back: ",q.back())
q.display()
