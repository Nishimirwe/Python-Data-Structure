li=[[10,20,45,30],[40,50,60,45],[21,70,80,90]]
maxInt=999999
def rotate(li):
    arr=({})
    for col in range(len(li[0])):
        arr.update({col:[maxInt]})
    for row in range(len(li)):
        for col in range(len(li[0])):
            arr[col].append(li[row][col])
    nInd=len(li[0])
    newArr=({nInd:[]})
    for col in range(len(li[0])):
        arr[col].remove(maxInt)
        arr[col].reverse()
        newArr[nInd].extend(arr[col])
    return newArr

newData=rotate(li)
count=0
for i in newData.keys():
    for j in newData[i]:
        print(j," ",end=' ')
        count+=1
        if(count%i==0):
            print()


        