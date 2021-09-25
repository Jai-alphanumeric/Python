# Writing the String oppositely using recursion
def invertion(a, b):
    if b > 0:
        print(a[b], end='')
        invertion(a, b - 1)
    elif b == 0:
        print(a[0])


string_to_invert = input('Enter the String : ')
invertion(string_to_invert, len(string_to_invert) - 1)
