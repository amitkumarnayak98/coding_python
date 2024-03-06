def count_triplets(arr):
    arr.sort() #Sorting takes 0(N log N) time

    triplet_count = 0

    for i in range(len(arr) - 1, 1, -1):
        left, right = 0, i - 1
        
        while left < right: 
            if arr[left] + arr[right] == arr[i]:
                triplet_count += 1
                left += 1
                right -= 1
                
            elif arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1
                
    return triplet_count

def main():
    
    #Get user input for the size of the array
    N = int(input("Enter the size of the array: "))
    
    if N <= 0:
        print("Invalid size. Please eneter a positive size.")
        return
    
    #Get user input for each element of the array
    arr = []
    print("Enter the elements of the array: ")
    
    for i in range(N):
        arr.append(int(input(f"Enter element {i + 1}: ")))
        
    #Print the entered array
    print("Entered array:", arr)
    
    #Measure the execution time
    import time 
    start_time = time.time()
    
    #Call the function or perform the computation
    triplets_count = count_triplets(arr)
    
    #Measure the execution time
    end_time = time.time()
    
    # Print the count of triplets with the required sum
    print("Triplets count:", triplets_count)
    
    #Print the execution time
    execution_time = end_time - start_time
    print("Execution time:", execution_time,"seconds")
    
if __name__ == "__main__":
    main()