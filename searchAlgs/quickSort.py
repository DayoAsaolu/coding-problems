from time import sleep


def quickSort(arr):
    if len(arr) < 2: return arr
    

    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)

def printer(arr):
    for i in arr:
        sleep(1)
        print(i)


def main():
    
    arr = [1,2,3,4]
    print(arr)

    # print("sorted arr --> ",quickSort(arr))

    # printer(arr)
    return 0





main()

