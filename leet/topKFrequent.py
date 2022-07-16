def topKFrequent(nums, k):

    uniqueNums = {}
    
    for i in nums:
        if i not in uniqueNums:
            uniqueNums[i]  = 1
        else:
            uniqueNums[i] +=1 
    
    sortedNums = sorted(uniqueNums, key= uniqueNums.get, reverse=True)
    
    
    return sortedNums[:k]

def main():
    nums1, k1 = [1,1,2,1,2,3], 2
    nums2, k2 = [1], 1
    nums3, k3 = [4,1,-1,2,-1,2,3], 2

    # print("topK -->", topKFrequent(nums1, k1))
    # print("topK -->", topKFrequent(nums2, k2))

    print("topK3 -->", topKFrequent(nums3, k3))
    return 0

main()