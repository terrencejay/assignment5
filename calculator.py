def addition():
    addition_result = number1 + number2
    print(addition_result)

def subtraction():
    sub = number1 - number2
    print(sub)

def multiply():
    multi = number1 * number2
    print(multi)

def division():
    if number2 != 0:
        divise = number1 / number2
        print(divise)
    else: 
        print("Can't divide by zero, try again")

while True:
   number1 = input("enter your first number or 'q' to quit: ")
   if number1.lower() == 'q':
       break
   operator = input("+,-,*,/")
   number2 = input("enter your second number: ")
   number1 = float(number1)
   number2= float(number2)
   
   if operator == "+":
       addition()
   elif operator == "-":
       subtraction()
   elif operator == "*":
       multiply()
   elif operator == "/":
       division()

   




   
   
