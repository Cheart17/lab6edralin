def main ():
    name = input("Enter your name: ")
    
name = input("Enter your name: ")
    
choice = input("Choose the type of conversion:\n1. Celcius to Fahrenheit\n2. Fahrenheit to Celcius\nEnter 1 or 2:")
    
if choice == '1':
    celsius = float(input("Enter temperature in Calcius: "))
    fahrenheit = (9/5) * celsius + 32
   
    print(f"Hello, {name}! {celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (5/9) * (fahrenheit - 32)
    print(f"Hello, {name}! {fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    
else:
    print("Invalid choice! please enter 1 or 2.")