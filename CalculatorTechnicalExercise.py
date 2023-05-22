def calculator():
    number1 = enter_number()  # Setting the first run through of the "enter_number()" function to be set to "number1"
    number2 = enter_number()  # Setting the second run through of the "enter_number()" function to be set to "number2"
    operator = select_operator(number2)  #
    result = calculate(number1,number2,operator) #
    print(number1, operator, number2, "equals", result) #Prints the result of the calculation for the user.
def enter_number(): #Function for user input of a number
    while(True): #A while loop that will repeat until it is told to stop.
        number = input("Enter number: ") #The input from the user is assigned to the variable "number".
        try:
            number = float(number) #Attempts to convert the variable "number" into a float.
        except:
            print("That isn't valid...") #If the value of "number" cannot be converted into a float then this text is printed.
            continue #This restarts the While loop so that the user can enter another value for "number"
        else:
            break #If the value for "number" is valid then this ends the While loop.
    return number #Returns the value of the function back to the caller

def select_operator(checkNumber): #Function to select the operation that will be applied to the inputted numbers
    while(True):
        operator = input("Please enter an operator, either +, -, /, *: ") #The input from the user is assigned to the variable "operator".

        if (operator=='/' and checkNumber==0):
            print("Can't divide by zero")
            continue

        validOperators=('+','-','*','/')

        if operator in validOperators: #If the variable "operator" is equal to any og the inputs then continue
            break

        else:
            print("That isn't valid...")
            continue

    return operator

def calculate(number1,number2,operator): #Function for the calculations between the "number" variable with the "operator" vairable stating what should be done with the two numbers
    if operator == "+":
        result = (number1 + number2) #If the variable "operator" is equal to "+" then the two numbers will be added together
    elif operator == "-": #elif is used so that once the operator is equal to the same operator entered in the variable "operator" so rest of the code in this function wont be executed as its not needed.
        result = (number1 - number2)
    elif operator == "/":
        result = (number1 / number2)
    elif operator == "*":
        result = (number1 * number2)
    return result

def converter(): #Function for converting between units
    while(True):
        selectedConversion = input("Please enter a conversion: 1 for Kilos to Stone, 2 for Gigabytes to Bytes, 3 for Inches to Centimetres, 4 for Days to Seconds: ")

        if (selectedConversion=="1"):
            factor = 5
            fromUnit = "Kilos" #The unit that the user will enter.
            toUnit = "Stone" #The unit that the entered number will be converted to.
            break
        elif (selectedConversion=="2"):
            factor = 1024*1024
            fromUnit="Gigabytes"
            toUnit="Bytes"
            break
        elif (selectedConversion=="3"):
            factor = 2.54
            fromUnit = "Inches"
            toUnit = "Centimetres"
            break
        elif (selectedConversion=="4"):
            factor = 24*3600
            fromUnit="Days"
            toUnit="Seconds"
            break
        else:
            print("This isn't valid...")
            continue

    while (True):
        prompt = "Enter "+fromUnit+": " #Sets "prompt" to equal the users input of their chosen conversion.
        number = input(prompt)  # The input from the user is assigned to the variable "number".

        try:
            number = float(number) #Attempts to convert the variable "number" into a float.
        except:
            print("That isn't a valid number...") #If the value of "number" cannot be converted into a float then this text is printed.
            continue #This restarts the While loop so that the user can enter another value for "number"
        else:
            break #If the value for "number" is valid then this ends the While loop.

    result=convert(number,factor) #Sets "result" to equal the product of number and factor from the function "convert"

    print(number, fromUnit, "is equal to",result,toUnit)  # Prints the result of the conversion for the user.

def convert(number,factor):
    return number * factor #Function for calculating "return".
def choice():
    while(True):
        choice = input("Please choose 1 for the Calculator and 2 for the Converter: ")# Giving the user choice between modes

        if choice == "1" or choice == "2":
            break

        else:
            print("That isn't valid...")
            continue
    return choice

choice = choice()

if choice == "1": #Calls the function calculator if the "choice" variable is equal to 1.
    calculator()

elif choice == "2":
    converter()






