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

def select_operator(): #Function to select the operation that will be applied to the inputted numbers
    while(True): #A while loop that will repeat until it is told to stop.
        operator = input("Please enter an operator, either +, -, /, *: ") #The input from the user is assigned to the variable "operator".

        if operator == "+" or operator == "-" or operator == "/" or operator == "*": #If the variable "operator" is equal to any og the inputs then continue
            break #Ends the loop
        else:
            print("That isn't valid...") #If the value of "operator" doesn't equal (+, -, /, *) then this text is printed
            continue #Restarts the loop to obtain a valid input.

    return operator #Returns the value of the function back to the caller

def calculate(): #Function for the calculations between the "number" variable with the "operator" vairable stating what should be done with the two numbers
    if operator == "+":
        result = (number1 + number2) #If the variable "operator" is equal to "+" then the two numbers will be added together
    elif operator == "-": #elif is used so that once the operator is equal to the same operator entered in the variable "operator" so rest of the code in this function wont be executed as its not needed.
        result = (number1 - number2)
    elif operator == "/":
        result = (number1 / number2)
    elif operator == "*":
        result = (number1 * number2)
    return result #Returns the value of the function back to the caller

number1 = enter_number() #Setting the first run through of the "enter_number()" function to be set to "number1"
number2 = enter_number() #Setting the second run through of the "enter_number()" function to be set to "number2"
operator = select_operator() #
result = calculate() #
print(number1, operator, number2, "equals", result) #Prints the result of the calculation for the user.


