import re


def main():
    y = [10, 5, 2, 3]
    print(quickSort(y))
    return 0

    
def recurvicSum(x):
    if len(x) == 0:
        print("this line")
        return 0
    if len(x) == 1:
        return 1    
    else:
        return x[0] + sum(x[1:])

def quickSort(x):
    if len(x) == 0:
        return [] # 0
    if len(x) == 1:
        return x
    elif len(x) == 2:
        return [min(x), max(x)]
    else:
        p = x[0]
        less, great = [], []
        for i in x[1:]:
            if i <= p:
                less.append(i)
            else:
                great.append(i)

        print("less and great", less, "--", great)
        return quickSort(less) + [p] + quickSort(great)

main()