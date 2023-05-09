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
#Make the user input numbers
#Add the numbers
#Subtract the numbers
#Multiply the numbers
#Divide the number
#Print the result of the operation
#Ask the user if they want to calculate another set of numbers
#End the program if the user wished to.
#Error handling