# Python code to demonstrate
# call by value
strng = "Geeks"

def test(st):
    strng = "GeeksforGeeks"
    print("Inside Function:", strng)

# Driver's code
test(strng)
print("Outside Function:", strng)
