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


