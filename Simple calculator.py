#Guide
print("Calculator operation")
print("Type 1 if you want to use Addition")
print("Type 2 if you want to use Subtraction")
print("Type 3 if you want to use Multiplication")
print("Type 4 if you want to use Division")

#Ask the user what operation they want to use
while True:
    operation = input("What operation would you like to use?: ")

    #check if the choice of the user is between 1-4
    if operation in ("1", "2", "3", "4"):

        #Add the numbers
        if operation == "1":
            print("Choice of operation: Addition")
            try:
                #Ask for their first and second number
                num1 = float(input("Please enter your first number:"))
                num2 = float(input("Please enter your second number:"))
                sum = num1 + num2
                print(sum)
            except ValueError:
                print("Invalid. Please try again")
        
        #Subtract the numbers
        elif operation == "2":
            print("Choice of operation: Subtraction")
            try:
                #Ask for their first and second number to subtract
                num1 = float(input("Please enter your first number:"))
                num2 = float(input("Please enter your second number:"))
                difference = num1 - num2
                print(difference)
            except ValueError:
                print("Invalid. Please try again")
        
        #Multiply the numbers
        elif operation == "3":
            print("Choice of operation: Multiplication")
            try:
                #Ask for their first and second number to multiply
                num1 = float(input("Please enter your first number:"))
                num2 = float(input("Please enter your second number:"))
                product = num1*num2
                print(product)
            except ValueError:
                print("Invalid. Please try again")
        
        #Divide the numbers
        elif operation == "4":
            print("Choice of operation: Division")
            try:
                #Ask for their first and second number to divide
                num1 = float(input("Please enter your first number:"))
                num2 = float(input("Please enter your second number:"))
                quotient = num1/num2
                print(quotient)
            except ValueError:
                print("Invalid. Please try again")

    #Ask the user if they want to do another calculation
    another_calculation = input("Do you want to do another calculation?(y/n)") 
    if another_calculation == "n":
        print("Thank you for using this calculator")  
    else:
        print("Proceeding to another calculation")    
        break