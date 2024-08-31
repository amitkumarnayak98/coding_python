def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    if low <= high:
        mid = low + (high - low) // 2
        
        #Check if target is present at mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            #Check if target is greater than mid element of array then ignore the left half of array
             low = mid + 1
             return low
        else:
            #Check if target is less than mid element of the array then ignore the right half of the array
            high = mid - 1
            return high
    else:
        return -1

def get_index_of_element(arr, n, target):
    for i in range(n):
        if(arr[i] == target):
            return i
        
    return -1
        
            

def main():
    #Get the user input for the size of the array
    n = int(input("Enter the size of the array: "))
    
    if n <= 0:
        print("Invalid size. Please enter a positive size.")
        return
    
    #Get user input for each element of the array
    arr = []
    print("Enter the elements of the array: ")
    
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))
        
    #Print the entered array
    print("Entered array[]: ", arr)
    
    arr.sort()
    
    print("Sorted array[]: ", arr)
    
    #Take input for the element to be searched
    target = int(input("Enter the element to search: "))
    
    #Performing binary search
    result = binary_search(arr, target)
    
    e = get_index_of_element(arr, n, target)
    
    if result != -1:
        print(f"Element found at index {e + 1}.")
    else:
        print("Element not found in the array.")
    

if __name__ == "__main__":
    main()