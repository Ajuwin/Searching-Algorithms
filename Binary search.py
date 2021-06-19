def binary_search(arr, x):
    
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return f'Element found at: {mid}'

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return 'Element not found'

# Driver code
arr = [2, 3, 4, 10, 40] 
x = 3
print(binary_search(arr, x))
