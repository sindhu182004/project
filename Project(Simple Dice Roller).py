import random


def roll_dice():
    print("Welcome to the Dice Roller!")
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            sides = int(input("Enter the number of sides on each die: "))

            if num_dice <= 0 or sides <= 0:
                print("Please enter positive numbers for dice and sides.")
                continue

            print(f"\nRolling {num_dice} d{sides}...")
            results = [random.randint(1, sides) for _ in range(num_dice)]
            print("Results:", results)
            print(f"Total: {sum(results)}\n")

        except ValueError:
            print("Please enter valid numbers.")

        again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


# Run the dice roller
roll_dice()