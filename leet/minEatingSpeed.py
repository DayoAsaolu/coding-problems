
import math

def minEatingSpeed(piles, h):
    def calHours( piles, k):
        total = 0
        for i in piles:
            temp = i/k
            total += math.ceil(temp)
        return total



    l, r = 1, max(piles)
    kokoSpeed = r

    while l <= r:
        mid = (l+r) // 2
        

        hours = calHours(piles, mid)
        if hours <= h:
            kokoSpeed = min(mid, kokoSpeed)

            r = mid -1
        else:
            l = mid+1
    

    return kokoSpeed


def main():
    piles, h = [3,6,7,11], 8
    piles1, h1 = [30,11,23,4,20], 5
    piles2, h2 = [30,11,23,4,20], 6

    print("min Eating Speed -->", minEatingSpeed(piles,h))
    print("min Eating Speed -->", minEatingSpeed(piles1,h1))
    print("min Eating Speed -->", minEatingSpeed(piles2,h2))
    return 0

main()
