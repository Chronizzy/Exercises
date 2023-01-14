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

def AnsRem(x, f1, f2, cc):
    printables = ''
    answerables = x
    if cc in ('increment','addition'):
        printables = (f1, '+', f2, '=', x)
    if cc in ('decrement', 'subtraction'):
        printables = (f1, '-', f2, '=', x)
    if cc in ('division' or 'half'):
        printables = (f1, '/', f2, '=', x)
    if cc in ('multiplication' or 'double'):
        printables = (f1, '*', f2, '=', x)
    print(printables) 
    reinputter('Wanna use this answer for ur next calculation?: YS/NO \n Choice: ', 'unkown', answerables, 'unkown')
    

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
                answer = (calculator(firstNumber, secondNumber, choice))
                AnsRem(answer, firstNumber, secondNumber, choice)
        if choice in ('double', 'half', 'increment', 'decrement'):
            if firstNumber == 'unknown':
                firstNumber = float(invoer)
                answer = (calculator(firstNumber, secondNumber, choice))
                if choice in ('half', 'double'):
                    AnsRem(answer, firstNumber, 2, choice)
                else:
                    AnsRem(answer, firstNumber, 1, choice)


        if choice == 'agane' and invoer not in ('subtraction', 'addition', 'multiplication', 'division', 'double', 'half', 'increment', 'decrement'):
            reinputter('thats not a choice cuh? try again: ' '\n  multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement\n Choice: ', choice, firstNumber, secondNumber)
        
    except:
        if invoer in ('subtraction', 'addition', 'multiplication', 'division'):
            choice = invoer
            
            
            try:
                float(firstNumber)              
                if choice == 'subtraction' and firstNumber != 'unknown':
                    reinputter(f'Choose the number you want to subtract from {firstNumber}: ', choice, firstNumber, secondNumber)
                if choice == 'addition' and firstNumber != 'unknown':
                    reinputter(f'Choose the number you want to add to {firstNumber}: ', choice, firstNumber, secondNumber)
                if choice == 'multiplication' and firstNumber != 'unknown':
                    reinputter(f'Choose the number you want to multiply by {firstNumber}: ', choice, firstNumber, secondNumber)
                if choice == 'division' and firstNumber != 'unknown':
                    reinputter(f'Choose the number you want to devide by {firstNumber}: ', choice, firstNumber, secondNumber)
            except:
                if firstNumber == 'unknown':
                    reinputter('Choose first number: ', choice, firstNumber, secondNumber)

        if invoer in ('double', 'half', 'increment', 'decrement'):
            choice = invoer

            try:
                float(firstNumber)           
                if choice == 'half' and firstNumber != 'unknown':
                    answer = (calculator(firstNumber, 2, choice))
                    AnsRem(answer, firstNumber, 2, choice)
                if choice == 'double' and firstNumber != 'unknown':
                    answer = (calculator(firstNumber, 2, choice))
                    AnsRem(answer, firstNumber, 2, choice)
                if choice == 'increment' and firstNumber != 'unknown':
                    answer = (calculator(firstNumber, 1, choice))
                    AnsRem(answer, firstNumber, 1, choice)
                if choice == 'decrement' and firstNumber != 'unknown':
                    answer = (calculator(firstNumber, 1, choice))
                    AnsRem(answer, firstNumber, 1, choice)
            except:                         
                if firstNumber == 'unknown':
                    reinputter(f'Choose the number you want to {choice}: ', choice, firstNumber, secondNumber)
            

        if invoer.capitalize() == 'Y':
            reUse('y')
        if invoer.capitalize() == 'N' or invoer.lower() == 'no':
            exit()
        if invoer.lower() == 'ys':
            print(firstNumber)
            reUseAns(firstNumber)

        else:
            reinputter('Wanna go again?: Y/N ', choice, firstNumber, secondNumber)
            
def reUseAns(x):
    reinputter(f'What do you want to do with: {x}?\n multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement\n Choice: ', 'agane', float(x), 'unknown')

def reUse(x):
    if x == 'y':
        reinputter(('Choose ur method: \n multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement\n Choice: '), 'agane','unknown', 'unknown')
    if x == 'n':
        exit()
    else:
        reinputter('Choose ur method: \n multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement\n Choice: ', 'agane','unknown', 'unknown')

reinputter('Choose ur method: \n multiplication\n addition\n division\n subtraction\n double\n half\n increment\n decrement\n Choice: ', 'agane','unknown', 'unknown')