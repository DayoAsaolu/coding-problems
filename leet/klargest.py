
def findkthlargest(nums, k):
    mid = len(nums) //2
    pivot = nums[mid]
    k_smallest = len(nums) - k
    # nums = quickselect(nums,1,k_smallest, 0)

    nums = quicksort(nums,1,k_smallest)
    print("nums--",nums)
    return nums[k]

def quickselect(nums, k, k_smallest, pivot_index):
    return 0
    

def quicksort(nums, k, pivPos):
    # print("pivPos--> ",pivPos)

    if len(nums) == 1:return nums
    if len(nums) == 0:return []

    if len(nums) < 3:
        return [min(nums[0], nums[1]), max(nums[0], nums[1])]

    mid = len(nums) //2
    pivot = nums[mid]
    nums = nums[:mid:] + nums[mid+1::]

    less = [i  for i in nums if i <= pivot]
    great = [i  for i in nums if i > pivot]

    print("%d iteration -- less=" % (k) , less, " pivot=", pivot, " great=", great)
    print()

    return quicksort(less, k=k+1, pivPos=1) + [pivot] + quicksort(great, k=k+1, pivPos=1)


def findKthLargest_leet(nums, k):
    """
    Quick Select using quicksort
    """
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
        
        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]  
        
        return store_index
    
    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:       # If the list contains only one element,
            return nums[left]   # return that element
        
        # select a random pivot_index between 
        pivot_index = random.randint(left, right)     
                        
        # find the pivot position in a sorted list   
        pivot_index = partition(left, right, pivot_index)
        
        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
                return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest 
    return select(0, len(nums) - 1, len(nums) - k)


def main():
    nums = [3,2,1,5,6,4]
    k = 2
    
    print(findkthlargest(nums,-k))
    
    return 0

main()