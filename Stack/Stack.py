class stack:
    def __init__(self):
        self.li=list()
        self.s=-1
        self.reset=-1010101

    #add
    def push(self,value):
        self.s+=1
        self.li.append(value)

    #peek
    def peek(self):
        return self.li[self.s]

    #pop
    def pop(self):
        x=self.li[self.s]
        self.li[self.s]=self.reset
        self.s-=1
        return x

    #view
    def display(self):
        for i in range(self.s+1):
            print(self.li[i],"::",end='')
        print()
        print("Size: ",self.s+1)

st=stack()
st.push(12)
st.push(43)
st.push(50)
st.push(55)
st.display()
print(st.peek()," ",st.pop())
st.display()

