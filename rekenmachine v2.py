def calculator(f1, f2, c):
    def subtraction(a, b):
        return a-b, 
    def addition(a, b):
        return a+b
    def multiplication(a, b):
        return b*a
    def division(a, b):
        return a/b

    if c == 'subtraction':
        return subtraction(f1, f2)
    if c == 'addition':
        return addition(f1, f2)
    if c == 'multiplication':
        return multiplication(f1, f2)
    if c == 'division':
        return division(f1, f2)
    if c == 'decrement':
        return subtraction(f1, 1)
    if c == 'increment':
        return addition(f1, 1)
    if c == 'double':
        return multiplication(f1, 2)
    if c == 'half':
        return division(f1, 2)


def reinputter(inputtable, globalChoiceReIN, globalFirstNumberReIN, globalSecondNumberReIN):
    invoer = input(inputtable)
    choice = globalChoiceReIN
    firstNumber = globalFirstNumberReIN
    secondNumber = globalSecondNumberReIN
    try:
        float(invoer)
        if choice in ('subtraction', 'addition', 'multiplication', 'division'):
            if firstNumber == 'unknown':
                firstNumber = float(invoer)
                reinputter('Choose second number: ', globalChoiceReIN, firstNumber, secondNumber)
            if secondNumber == 'unknown':
                secondNumber = float(invoer)
                print(calculator(firstNumber, secondNumber, choice))
        if choice in ('double', 'half', 'increment', 'decrement'):
            if firstNumber == 'unknown':
                firstNumber = float(invoer)
                print(calculator(firstNumber, secondNumber, choice))

        if choice == 'agane' and invoer not in ('subtraction', 'addition', 'multiplication', 'division', 'double', 'half', 'increment', 'decrement'):
            reinputter('thats not a choice cuh? try again: ' '\n  multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement:  ', choice, firstNumber, secondNumber)
        
    except:
        if invoer in ('subtraction', 'addition', 'multiplication', 'division'):
            choice = invoer
            reinputter('Choose first number: ', choice, firstNumber, secondNumber)
        if invoer in ('double', 'half', 'increment', 'decrement'):
            choice = invoer
            reinputter(f'Choose the number you want to {choice}; ', choice, firstNumber, secondNumber)
        if invoer.capitalize() == 'Y':
            reUse('y')
        if invoer.capitalize() == 'N':
            exit()
        else:
            reinputter('Wanna go again?: Y/N ', choice, firstNumber, secondNumber)
            


def reUse(x):
    if x == 'y':
        reinputter(('Choose ur method: \n multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement\n: '), 'agane','unknown', 'unknown')
    if x == 'n':
        exit()
    reinputter('Again?: ', 'agane','unknown', 'unknown')

reinputter('Choose ur method: \n multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement :  ', 'agane','unknown', 'unknown')