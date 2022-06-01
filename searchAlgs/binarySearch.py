def binarySearch(arr ,target):
    start, mid, end = 0, len(arr)//2, len(arr)-1

    guess = arr[mid]

    while start <= end:
        if guess == target:
            return [mid, arr[mid]]
        elif guess < target:
            start = mid+1
        else:
            end = mid-1

        mid = (start +end) // 2
        guess = arr[mid]        

        print("start, end, mid--> ",start,"--", end, "--", mid)
        # if start == 2: break

    return -1

def main():
    x = [1,3,5,7,9,11,13,17,19,23]

    print(binarySearch(x, 4))
    return 0

main()
