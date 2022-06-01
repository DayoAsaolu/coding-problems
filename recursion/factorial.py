def factorial(n):
    if n == 0: return 1
    if n == 1: return 1

    return n * factorial(n-1)

def add(arr):
    if len(arr) == 1: return arr[0]

    return arr[-1] + add(arr[:-1:])

def count(arr):
    if len(arr) == 0: return 0
    if len(arr) == 1: return 1

    return 1 + count(arr[:-1:])



def main():
    # print("factorial--> ", factorial(4))
    x = [1,2,3,4]

    
    # print("count -->", count(x))
    # print("add--> ",add(x))

    

    return 0





main()

