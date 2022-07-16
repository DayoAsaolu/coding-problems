def containsDup2(nums):
    return len(set(nums)) != len(nums)


def containsDuplicate(nums) -> bool:
    '''
    dict to store unique
    loop thorough nums
        check n in unique
            return false
        add it to unique
    '''
    
    unique = {}
    
    for i in nums:
        if i in unique:
            return True
        else:
            unique[i] = None
            
    return False
    
        
        
def main():

    nums = [1,2,3,1]
    nums1 = [1,2,3]

    print("HasDuplicate -->", containsDuplicate(nums))
    print("HasDuplicate -->", containsDuplicate(nums1))

    return 0

main()

    