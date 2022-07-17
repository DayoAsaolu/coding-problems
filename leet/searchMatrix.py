def searchMatrix(matrix, target):
    def binarysearch(nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (r+l) //2 
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1

        return False

    for i in matrix:
        if binarysearch(i, target):
            return True
    

    return False


def main():
    matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
    matrix1, target1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],  13

    print("search Matrix -->", searchMatrix(matrix, target))
    print("search Matrix -->", searchMatrix(matrix1, target1))
    return 0

main()