# Simple Bank Balance Checker

balance = 6000023
correct_pin = 1234

pin = int(input("Enter your 4-digit PIN: "))

if pin == correct_pin:
    print("\nLogin Successful!")
    print("Your current bank balance is ₹", balance)
else:
    print("Incorrect PIN! Please try again.")

