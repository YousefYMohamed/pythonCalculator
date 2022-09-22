import time
# Fucntion to find if character in a string is part of a number
def isNumeral(char):
    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or  char == '7' or char == '8' or char == '9' or char == '.' or char == '-':
        return True
    else:
        return False


# Defining an addition function
def add(num1,num2):
    isnum1Decimal = False
    if isinstance(num1, str):  
        for c in num1:
            if c == ' ':
                num1.replace(' ','')
            elif c == '.' and isnum1Decimal == False:
                isnum1Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    isnum2Decimal = False
    if isinstance(num2, str):  
        for c in num2:
            if c == ' ':
                num2.replace(' ','')
            elif c == '.' and isnum2Decimal == False:
                isnum2Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    if isinstance(num1, str):  
        if isnum1Decimal:
            num1Value = float(num1)
        else:
            num1Value = int(num1)
    else:
        num1Value = num1
    
    if isinstance(num2, str):  
        if isnum2Decimal:
            num2Value = float(num2)
        else:
            num2Value = int(num2)
    else:
        num2Value = num2
        
    return num1Value + num2Value

# Defining a subtraction function
def sub(num1,num2):
    isnum1Decimal = False
    if isinstance(num1, str):  
        for c in num1:
            if c == ' ':
                num1.replace(' ','')
            elif c == '.' and isnum1Decimal == False:
                isnum1Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    isnum2Decimal = False
    if isinstance(num2, str):  
        for c in num2:
            if c == ' ':
                num2.replace(' ','')
            elif c == '.' and isnum2Decimal == False:
                isnum2Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    if isinstance(num1, str):    
        if isnum1Decimal:
            num1Value = float(num1)
        else:
            num1Value = int(num1)
    else:
        num1Value = num1
    
    if isinstance(num2, str):
        if isnum2Decimal:
            num2Value = float(num2)
        else:
            num2Value = int(num2)
    else:
        num2Value = num2
        
    return num1Value - num2Value
    
# defining a multiplication function
def mul(num1,num2):
    isnum1Decimal = False
    if isinstance(num1, str):
        for c in num1:
            if c == ' ':
                num1.replace(' ','')
            elif c == '.' and isnum1Decimal == False:
                isnum1Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    isnum2Decimal = False
    if isinstance(num2, str):
        for c in num2:
            if c == ' ':
                num2.replace(' ','')
            elif c == '.' and isnum2Decimal == False:
                isnum2Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    if isinstance(num1, str):
        if isnum1Decimal:
            num1Value = float(num1)
        else:
            num1Value = int(num1)
    else:
        num1Value = num1
    
    if isinstance(num2, str):
        if isnum2Decimal:
            num2Value = float(num2)
        else:
            num2Value = int(num2)
    else:
        num2Value = num2
    return num1Value * num2Value
    
    
# Defining a division function
def div(num1,num2):
    isnum1Decimal = False
    if isinstance(num1, str):
        for c in num1:
            if c == ' ':
                num1.replace(' ','')
            elif c == '.' and isnum1Decimal == False:
                isnum1Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    isnum2Decimal = False
    if isinstance(num2, str):
        for c in num2:
            if c == ' ':
                num2.replace(' ','')
            elif c == '.' and isnum2Decimal == False:
                isnum2Decimal = True
            elif not isNumeral(c):
                return "Error, incorrect input type"
    
    if isinstance(num1, str):
        if isnum1Decimal:
            num1Value = float(num1)
        else:
            num1Value = int(num1)
    else:
        num1Value = float(num1)
        
    if isinstance(num2, str):
        if isnum2Decimal:
            num2Value = float(num2)
        else:
            num2Value = int(num2)
    else:
        num2Value = float(num2)
        
    return num1Value / num2Value

def calc():
    while True:
        # initializing and printing the welcome message to user
        user_welcome_message = "Welcome to the calculator python program! \nPlease select the operation to perform: \nOnly [+,-,*,/] available->"
        print(user_welcome_message)
        
        equationStr = input()
        if equationStr == '+':
            print("Enter value 1:")
            val1 = input()
            print("Enter value 2:")
            val2 = input()
            
            print("---- Results ----")
            print(add(val1,val2))
        elif equationStr == '-':
            print("Enter value 1:")
            val1 = input()
            print("Enter value 2:")
            val2 = input()
            
            print("---- Results ----")
            print(sub(val1,val2))
        elif equationStr == '*':
            print("Enter value 1:")
            val1 = input()
            print("Enter value 2:")
            val2 = input()
            
            print("---- Results ----")
            print(mul(val1,val2))
        elif equationStr == '/':
            print("Enter value 1:")
            val1 = input()
            print("Enter value 2:")
            val2 = input()
            
            print("---- Results ----")
            print(div(val1,val2))
        else:
            print("Unidentified operation! Please choose another operation.")
            time.sleep(1)
        time.sleep(6)
if __name__ == "__main__":
    calc()