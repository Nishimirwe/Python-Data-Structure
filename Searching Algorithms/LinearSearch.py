#Linear search, we loop through an array and check if a value we want exist
#We use loop

#The function returns the index of tha value if found, otherwise return -1

def LinearSearch(names,value):
    for i in range(len(names)):
        if(names[i]==value):
            return i
    return -1

names=["Paul","Jean","Jane","Rashid","Japhet"]
print(LinearSearch(names,"Paul"))
