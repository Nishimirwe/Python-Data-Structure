#In strings, we use ord() function to use their ASCII values

class HashTable:
    def __init__(self,size):
        self.capacity=size
        self.strs=[None]*self.capacity
        self.length=[0]*self.capacity

    def isEmpty(self):
        if sum(self.length)==0:
            return True
        return False

    def isFull(self):
        if sum(self.length)==self.capacity:
            return True
        return False

    def hash(self,str):
        s=0
        for i in str:
            s+=ord(i)
        return s%self.capacity

    def add(self,str):
        if self.isFull():
            print("Full Hash Table")
        else:
            index=self.hash(str)
            if self.strs[index] is None:
                self.strs[index]=str
                self.length[index]+=1
            else:
                i=index
                while self.strs[index%self.capacity] is not None:
                    index+=1
                index=index%self.capacity
                self.strs[index]=str
                self.length[index]+=1

    def show(self):
        if self.isEmpty():
            print("Empty Hash Table")
        else:
            print(self.strs)
            print("Size: ",sum(self.length))

    def search(self,str):
        if self.isEmpty():
            return "Hash Table is Empty, No data"
        else:
            index=self.hash(str)
            if self.strs[index]==str:
                return str," is successfully found at index ",index
            else:
                i=index
                while self.strs[index%self.capacity]!=str:
                    index+=1
                    if index%self.capacity==i:
                        return str," could not be found, we are already truning back to the start", i
                index=index%self.capacity
                return str," is successfully found at index ",index


ht=HashTable(5)
ht.add("NISHIMIRWE")
ht.add("MWIZERWA")
ht.add("YVES")
ht.add("RASHID")
ht.add("MAMA")
ht.show()
print("Searching methods")
print(ht.search("MWIZERWA"))