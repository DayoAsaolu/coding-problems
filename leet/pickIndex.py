import random

class pick:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        print(self.total_sum)
        print(self.prefix_sums)

        target = self.total_sum * random.random()
        print(target)
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            print("i--target--prefix_sum ",i,"--", target, "--",prefix_sum)
            if target < prefix_sum:
                return i

def main():
    l = pick([1,2,3,4,5])
    print("pick index --> ", l.pickIndex())
    return 0

main()