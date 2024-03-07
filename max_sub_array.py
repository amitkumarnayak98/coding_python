#Calculate the sum of all elements of the array
def maxSubarraySum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for num in arr[1:]:
        #Choose between extending the current subarray or starting a new subarray
        current_sum = max(current_sum + num, num)
        
        #Update the maximum sum if the current sum is greater
        max_sum = max(current_sum, max_sum)
        
    return max_sum

def main():
    
    #Get the user input for the size of the array
    N = int(input("Enter the size of the array: "))
    
    if N <= 0:
        print("Invalid size. Please enter a positive size.")
        return
    
    #Get user input for each element of the array
    arr = []
    print("Enter the elements of the array: ")
    
    for i in range(N):
        arr.append(int(input(f"Enter element {i + 1}: ")))
        
    #Print the entered array
    print("Entered array[]: ", arr)
    
    #Measure the execution start time
    import time
    start_time = time.time()
    
    max_sum = maxSubarraySum(arr)
    
    #Measure the execution end time
    end_time = time.time()
    
    print(f"Max subarray sum is {max_sum} of elements {arr} which is a contiguous subarray.") 
    
    #Print the execution time
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    
    
if __name__ == "__main__":
    main()