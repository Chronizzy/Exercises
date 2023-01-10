
firstNumber = 0
secondNumber = 0
choice = 'again'
invoer = 'again'

def agane(badunka):
    if badunka == 'reset':
        reinputter('Do you wanna calculate again?: Y/N ')


def numberFunction(n2, n1):
    global choice
    def subtraction(a, b):
        return a-b
    def addition(a, b):
        return a+b
    def multiplication(a, b):
        return b*a
    def division(a, b):
        return a/b
    

    if choice == 'subtraction':
        choice = 'reset'
        return subtraction(n1, n2)
    if choice == 'addition':
        choice = 'reset'
        return addition(n1, n2)
    if choice == 'multiplication':
        choice = 'reset'
        return multiplication(n1, n2)
    if choice == 'division':
        choice = 'reset'
        return division(n1, n2)



def reinputter(x):
    global firstNumber
    global secondNumber
    global choice
    global invoer
    invoer = input(x)
    try:
        float(invoer)
        x = float(invoer)
        if firstNumber  > 0 or firstNumber < 0:
            secondNumber = x
            print(numberFunction(firstNumber, secondNumber)  )
        else:
            firstNumber = x
            reinputter('choose second number: ')
    except:
        if invoer.lower() == 'n':
            calculator('stop')
        if invoer.lower() == 'y':
            firstNumber == 0
            secondNumber == 0
            choice == 'again'
            calculator(choice)
        if invoer == 'addition' or invoer == 'subtraction' or invoer == 'multiplication' or  invoer =='division':
            choice = invoer
            calculator(invoer.lower())
        if invoer == 'stop':
            calculator(invoer)
        else:
            reinputter('???')


def calculator(i):
    global choice
    if i == 'addition' or i == 'subtraction' or i == 'multiplication' or i =='division':
        reinputter('choose first number: ')
    if i == 'stop':
        return 
    if i == '' or i == 'again' :
        reinputter('What method of calculation do you want to use?: multiplication, addition, division, subtraction: ')

calculator(invoer)