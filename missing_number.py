#logic to find out the missing number from the array of the elements
def MissingNumber(arr, N):
    totalXOR = 0
    arrXOR = 0
    
    #XOR of all numbers from 1 to N
    for i in range(1, N + 1):
        totalXOR ^= i
        
    #XOR of array elements
    for num in arr:
        arrXOR ^= num
    
    return totalXOR ^ arrXOR

def main():
    
    #Get the user input for the size of the array
    N = int(input("Enter the size of the array: "))
    
    if N <= 0:
        print("Invalid state. Please enter a positive size.")
        return

    #Get the user input for each element of the array
    arr = []
    print("Enter the elements of the array: ")
    
    for i in range(N - 1):
        arr.append(int(input(f"Enter element {i + 1}: ")))
        
    #Print the entered array
    print("Entered array[]: ", arr)
    
    import time
    
    #Measure the execution start time
    start_time = time.time()
    
    missing_number = MissingNumber(arr, N)
    
    #Measure the execution end time
    end_time = time.time()
    
    print(f"Missing Number is {missing_number}")
    
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "milliseconds")
    
if __name__ == "__main__":
    main()