"""
Program: Simple Calculator 

Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

while True:
        try:
           number1=int(input("Insert the first value: "))
           if number1 == isinstance(number1, int):
             break
        except ValueError:
            print('You must enter a number')
            continue

        try:
           number2=int(input("Insert the second value: "))
           if number2 == isinstance(number2, int):
             break
        except ValueError:
            print('You must enter a number')
            continue

        print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
        select = input("Select operations form :")
        addition=number1+number2
        subtraction=number1-number2
        multiplication=number1*number2
        division=number1/number2



        if select == '1' or '+' :
              print(f"The addition for the two values is equal to: {addition}")

        elif select == '2' or '-' :
              print(f"The subraction for the two values is equal to: {subtraction}")

        elif select == '3' or '*' :
              print(f"The multiplication for the two values is equal to: {multiplication}")

        elif select == '4' or  '/' :
              print(f"The division for the two values is equal to: {division}")

        else:
              print("invalid input")
        
