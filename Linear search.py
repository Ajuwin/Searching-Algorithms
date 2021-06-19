def linear_search(arr, x):

    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return f'Element found at index: {i}'
            
    else:
        return "Element not found"

# Driver code

arr = [23, 56, 84, 12, 7, 64]
x = 84                        # Element to find
print(linear_search(arr, x))

