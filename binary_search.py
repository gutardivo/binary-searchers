def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")

