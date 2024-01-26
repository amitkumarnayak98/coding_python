def main():

    # Get user input for the range
    n = int(input("Enter the range (up to which number): "))

    # Validate input to ensure it's not negative
    if n <= 0:
        print("Please enter a positive number for the range.")
        return #Exit the programme
    
    # Define an array with size n
    numbers = list(range(1, n+1))

    # Print the array elements
    print("Array elements:", *numbers)

if __name__ == "__main__":
    main()