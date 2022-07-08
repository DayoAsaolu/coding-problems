def quicksort(intervals):
    if len(intervals) < 2:
        return intervals
    else:
        pivot = intervals[0]

        less = [i for i in intervals[1:] if i[0] <= pivot[0]]
        greater = [i for i in intervals[1:] if i[0] > pivot[0]]


        return quicksort(less) + [pivot] + quicksort(greater)


def merge(intervals):
    intervals = quicksort(intervals)
    print(intervals)

    merged = [ intervals[0] ]

    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max( merged[-1][1], intervals[i][1] )
        else:
            merged.append( intervals[i] )
        
    return merged

def main():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals1 = [ [1,4], [4,5] ]

    print("merged list -->",merge(intervals))
    print("merged list1 ->",merge(intervals1))
    return 0


main()