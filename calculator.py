#Saahil Patel
#Calculator

def add(num1, num2): 
    return num1 + num2 
  
def subtract(num1, num2): 
    return num1 - num2 
  
def multiply(num1, num2): 
    return num1 * num2 
  
def divide(num1, num2): 
    return num1 / num2 

def raisePower(x, y):
   return x ** y

print("Which Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Raising a power to number Like 2 sqr 5")

choice = input("Enter choice: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1, "+" ,num2, "=", add(num1, num2))

elif choice == '2':
   print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
   print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
   print(num1, "/", num2, "=", divide(num1, num2))

elif choice == '5':
   print(num1, "**", num2, "=", raisePower(num1, num2))

else:
   print("Please select a valid input.")