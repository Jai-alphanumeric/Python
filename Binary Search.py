# Binary Search in a sorted array
def bin(v, k):
    low = 0
    high = len(v) - 1
    while low <= high:
        mid = int((low + high)/2)
        if k == v[mid]:
            return mid
        elif k < v[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -999


a = [1, 3, 5, 7, 8, 9, 12]
i = int(input('Enter the digit that you want to find in the array : '))
r = bin(a, i)
if r >= 0:
    print(i, 'found at', r, 'index value')
else:
    print('Sorry !', i, 'not found in array')

