# correct but too slow  -- 0(n3)
def longestConsecutive(nums):
    longest = 0
    for i in nums:
        count = 0
        curr = i

        while curr in nums:
            count += 1
            curr += 1

        longest = max(count, longest)

    return longest

# optimal solution
def longestConsecutivev2(nums):


    return 0

def main():
    nums1 = [ 100, 4, 200, 1, 3, 2 ]
    nums2 = [0,3,7,2,5,8,4,6,0,1]

    print("nums1 -->", longestConsecutive(nums1))
    print("nums2 -->", longestConsecutive(nums2))

    return 0

main()