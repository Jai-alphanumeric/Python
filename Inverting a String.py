# Writing the String oppositely using recursion
def invertion(a, b):
    if b > 0:
        print(a[b], end='')
        invertion(a, b - 1)
    elif b == 0:
        print(a[0])


string_to_inert = input('Enter the String : ')
invertion(string_to_inert, len(string_to_inert) - 1)
