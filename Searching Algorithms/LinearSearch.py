#Linear search, we loop through an array and check if a value we want exist
#We use loop

def LinearSearch(names,value):
    for i in names:
        if(i==value):
            return "Found"
    return "Not Found"

names=["Paul","Jean","Jane","Rashid","Japhet"]
print(LinearSearch(names,"Paula"))
