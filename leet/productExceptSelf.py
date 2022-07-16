#brute force
def productExceptSelf(nums):
    ans = []

    for i in range(len(nums)):
        temp = 1
        sublist = nums[:i] + nums[i+1:]
        for i in sublist:
            temp *= i
        ans.append(temp)

    return ans

# optimal 1
def productSelf(nums):
    def help(nums, i):
        sublist = nums[:i] + nums[i+1:]

        temp = sublist[0]
        for i in sublist[1:]:
            temp *= i 

        return temp

    first = nums[1]
    
    for i in nums[2:]:
        first *= i
    ans = [ first ]
    t = first * nums[0]

    for i in range(1, len(nums)):
        if first == 0:
            if nums[i] != 0:
                ans.append(0)
            else:
                ans.append(help(nums, i))
        else:
            ans.append(t//nums[i])

    return ans


# optimal 2
def productSelf1(nums):
    res = [1] * (len(nums))
        
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    print("res -->",res)

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def main():
    nums1 = [1,2,3,4]
    nums2 = [4,3,2,1,2]

    print("produ -->", productSelf1(nums1))
    # print("produ -->", productSelf1(nums2))
    return 0

main()