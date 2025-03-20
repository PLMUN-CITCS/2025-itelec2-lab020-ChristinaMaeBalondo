# BALONDO, CHRISTINA MAE L.
# ITELECT2
# Laboratory #20 - Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python 

def main():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":  # Fixed spacing
    main()
