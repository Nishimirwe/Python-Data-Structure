class Node:
    def __init__(self,value):
        self.data=value
        self.Next=None

class Stack:
    def __init__(self):
        self.Head=None
        self.s=0
    #add
    def push(self,value):
        node=Node(value)
        if not self.Head:
            self.Head=node
            self.s+=1
        else:
            node.Next=self.Head
            self.Head=node
            self.s+=1
    #pop
    def pop(self):
        if not self.Head:
            return "Empty List", -1
        else:
            x=self.Head.data
            self.Head=self.Head.Next
            self.s-=1
            return x
    #empty
    def isEmpty(self):
        if not self.Head:
            return True
        return False
    #peek
    def peek(self):
        if not self.Head:
            return "Empty List", -1
        return self.Head.data
    #display
    def display(self):
        if not self.Head:
            print("Empty List")
        else:
            nav=self.Head
            while nav:
                print(nav.data,"::",end='')
                nav=nav.Next
            print()
            print("Size: ",self.s," Head: ", self.Head.data)
    #Delete
    def delete(self):
         self.Head=None

st=Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.display()
st.pop()
st.display()

