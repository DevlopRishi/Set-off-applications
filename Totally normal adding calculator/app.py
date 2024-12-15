import random
import time

def add_only_calculator():
    """A calculator that can only add, but with glitches."""
    print("Welcome to the Glitchy Addition-Only Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number (or maybe not?): "))
            num2 = float(input("Enter the second number (if you're lucky): "))

            if random.random() < 0.2:  # 20% chance of a glitch before calculation
                print("Oops! The numbers seem to have...shifted.")
                num1 = num1 + random.uniform(-5,5)
                num2 = num2 + random.uniform(-5,5)
            
            if random.random() < 0.1: # 10% Chance of a catastrophic glitch
                print("Oh no the calculator got confused. It can't remember how to add")
                print(f"The result is: {random.choice(['ERROR','NAN','Infinity','-Infinity'])}")
                continue

            result = num1 + num2
            print(f"The result, if you trust it: {result}")
        except ValueError:
            print("Invalid input or was it? Try again!")

        time.sleep(random.uniform(0,2))

        continue_calc = input("Try again? (y/n): ").lower()
        if continue_calc != "y":
            break
        if random.random() < 0.2:
          print("Fine by me, not like I wanted to calculate anything anyway...")
          break

if __name__ == "__main__":
    add_only_calculator()