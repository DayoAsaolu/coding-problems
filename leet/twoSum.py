def twoSum(nums, target):

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums:
            return [i, nums.index(diff)]


def main():
    x = [2,]

    return 0


main()