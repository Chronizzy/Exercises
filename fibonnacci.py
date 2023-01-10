
amount = int(input("dawg: "))
amountLeft = amount

def fib(n, y):
    global amountLeft
    amountLeft -= 1
    if amountLeft != -1 and amount > 0:
        print(n, y)
        return (fib(n+y, y+(n+y)))


    
fib(0,1)