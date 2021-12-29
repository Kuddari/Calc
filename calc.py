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
select = int(input("Select operations form 1, 2, 3, 4 :"))
number1=int(input("Insert the first value"))
number2=int(input("Insert the second value"))


addition=number1+number2
subtraction=number1-number2
multiplication=number1*number2
division=number1/number2



if select == 1:
       print(f"The addition for the two values is equal to: ,{addition}")

elif select == 2:
       print(f"The subraction for the two values is equal to: ,{subtraction}")

elif select == 3:
       print(f"The multiplication for the two values is equal to: ,{multiplication}")

elif select == 4:
        print(f"The division for the two values is equal to: ,{division}")

else:
        print("invalid input")
        
