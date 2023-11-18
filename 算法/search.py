def search(list, key):
    low, high = 0, len(list)-1
    # while True:
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < key:
            low = mid + 1
        elif list[mid] > key:
            high = mid - 1
        else:
            return mid
 
l = [1, 2, 3, 4, 5, 6, 8, 9]       
print("key:", search(l, 1))