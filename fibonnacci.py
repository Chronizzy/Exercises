amount = int(input("dawg: "))

def fib(n, y, z):
    amountLeft = z
    if amountLeft != -1 and amount > 0:
        print(n, y)
        amountLeft -= 1
        return (fib(n+y, y+(n+y), amountLeft))


    
fib(0,1, amount)