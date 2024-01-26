def find_subarray_with_sum(arr, target_sum):
    start = 0
    current_sum = 0

    for end, num in enumerate(arr):
        current_sum += num

        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target_sum:
            return start + 1, end + 1  # Adjust to 1-based indexing

    return -1,  # Return -1 if no subarray is found

def main():
    # Get user input for the range
    n = int(input("Enter the range (up to which number): "))

    # Validate input to ensure it's not negative
    if n <= 0:
        print("Please enter a positive number for the range.")
        return  # Exit the program

    # Get user input for the target sum
    target_sum = int(input("Enter the target sum: "))

    # Create an array with numbers from 1 to n
    numbers = list(range(1, n + 1))

    # Find subarray with the target sum
    result = find_subarray_with_sum(numbers, target_sum)

    # Print the result
    if result[0] == -1:
        print("-1")
    else:
        print(f"The sum of elements from {result[0]} position to {result[1]} position is {target_sum}")

if __name__ == "__main__":
    main()
