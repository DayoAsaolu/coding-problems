# in progress

def search(nums, target):
    l, r = 0, len(nums) -1

    while l <= r:
        

        mid = (l + r) //2 
        print("start --- l, r, mid -- %d, %d, %d", l, r, mid)

        if nums[mid] == target: return mid
        current = nums[mid]


        if target <= current:
            if target > current:
                l = mid +1
            else:
                pass
        else:
            pass
            

        print("end --- l, r, mid -- %d, %d, %d", l, r, mid)

    return -1 

def main():
    nums, target = [4,5,6,7,0,1,2], 0
    nums1, target1 = [4,5,6,7,0,1,2],  3
    nums2, target2 = [1],  0
    nums3, target3 = [1,3],  3

    # print("found in array - index ->>", search(nums, target))
    # print("found in array - index ->>", search(nums1, target1))
    # print("found in array - index ->>", search(nums2, target2))

    print("found in array - index ->>", search(nums3, target3))
    return 0 


main()

