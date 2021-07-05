#This algorithm saves tha value at the index=value
# It might use large space because lenght of array should be equal maybe (min+max+1)*2 worst case, when some numbers are less than zero
def mySort(li,mi,ma):
    size=((ma-mi)+1)
    arr=[None]*size
    for i in li:
        arr[i]=i
    for j in arr:
        if j is not None:
            print(j,"->",end='')
    print()

ar=[34,56,2,89,0,-1]
mySort(ar,0,100)


