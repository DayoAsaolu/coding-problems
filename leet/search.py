def search(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (r+l) //2 
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid-1
        else:
            l = mid+1

    return -1


def main():
    nums1, target1 = [-1,0,3,5,9,12], 9
    nums2, target2 = [-1,0,3,5,9,12], 2

    print("searcher -->", search(nums1, target1))
    print("searcher -->", search(nums2, target2))

    return 0

main()