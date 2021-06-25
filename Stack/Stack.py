class stack:
    def __init__(self):
        self.li=list()
        self.s=-1
        self.reset=-10101

    #isEmpty
    def isEmpty(self):
        if self.s<0:
            return True
        return False

    #add
    def push(self,value):
        self.s+=1
        self.li.append(value)

    #peek
    def peek(self):
        if not self.isEmpty():
            return self.li[self.s]
        return "Empty List", -1
    #pop
    def pop(self):
        if not self.isEmpty():
            x=self.li[self.s]
            self.li[self.s]=self.reset
            self.s-=1
            return x
        return "Empty List", -1

    #view
    def display(self):
        if not self.isEmpty():
            for i in range(self.s+1):
                print(self.li[i],"::",end='')
            print()
            print("Size: ",self.s+1)
        else:
            print("Empty list")

    #destroy
    def destroy(self):
        self.s=-1
        self.li.clear()
st=stack()
st.push(12)
st.push(43)
st.push(50)
st.push(55)
st.destroy()
st.display()
print(st.peek()," ",st.pop())
st.display()

