li=[-11]*100
def fib(n):
    if n==0:
        li[n]=0
        return 0
    elif n==1:
        li[n]=1
        return 1
    if li[n]==-11:
        print("we are saving",n)
        li[n]=fib(n-1)+fib(n-2)
    return li[n-1]+li[n-2]

print(fib(50))
