def rotateRight(d, arr):
    # Write your code here
    L = len(arr)
    
    end = len(arr) -d
    rot = arr[-1:end-2:-1]
    rot = rot[-1::-1]
    arr = rot + arr
    
    return arr[:L:]


def rotateLeft(d, arr):
    # Write your code here
    rot = arr[:d:]
    arr = arr[d::] + rot
    
    return arr

def main():
    arr = [1,2,3,4,5]
    d = 4
    print(rotateLeft(d, arr))

    return 0 


main()