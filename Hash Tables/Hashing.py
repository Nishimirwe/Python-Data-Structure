#This is a hashing table that uses linear probing
def hash(value, s):
    return value%s
class HashTable:
    def __init__(self,size):
        self.capacity=size
        self.li=[None]*self.capacity
        self.length=[0]*self.capacity

    def isEmpty(self):
         if sum(self.length)==0:
             return True
         return False

    def isFull(self):
         if sum(self.length)==self.capacity:
             return True
         return False

    def add(self, value):
         if self.isFull():
             print("Full HashTable")
         else:
             index=hash(value,self.capacity)
             if self.li[index] is None:
                 self.li[index]=value
                 self.length[index]+=1
             else:
                i=index
                while self.li[index%self.capacity] is not None:
                    index+=1
                index=hash(index,self.capacity)
                self.li[index]=value
                self.length[index]+=1

    def show(self):
        if self.isEmpty():
            print("Empty HashTable")
        else:
           print(self.li)
           print(sum(self.length))

    def search(self,value):
        if self.isEmpty():
            return "Empty HashTable", -1
        else:
            index=hash(value,self.capacity)
            if self.li[index]==value:
                return "Found at index ",index
            else:
                i=index
                while self.li[hash(index,self.capacity)]!=value:
                    index+=1
                    if hash(index,self.capacity)==i:
                        return "Not Found at all, we returned on ",i, "Bro"
                return "Found at Index ",hash(index,self.capacity)

ht=HashTable(5)
ht.add(10)
ht.add(20)
ht.add(29)
ht.add(39)
ht.add(40)
ht.add(40)
ht.show()
print("Searching")
print(ht.search(9))
