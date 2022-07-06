# sorting
# approach 1 -- quicksort
def quicksort(intervals):
    if len(intervals) < 2: return intervals
    

    else:
        pivot = intervals[0]

        less = [i for i in intervals[1:] if i[0] <= pivot[0]]

        greater = [i for i in intervals[1:] if i[0] > pivot[0]]

        return quicksort(less) + [pivot] + quicksort(greater)

# approach 2 -- lambda and sorted funtion inbuilt
def inbuiltSort(intervals):
    return sorted(intervals, key=lambda x: x[0])

def canAttendMeetings(intervals):
    decision = True

    meeting = quicksort(intervals)

    for i in range(1,len(meeting)):
        if meeting[i][0] < meeting[i-1][1]:
            return False
    return decision


def minMeetingRooms(intervals):
    sortedIntervals = quicksort(intervals)

    numRooms = [sortedIntervals[0][1]]
    
    for i in range(1, len(sortedIntervals)):
        if sortedIntervals[i][0] >= numRooms[0]:
            numRooms.pop(0)
            numRooms.append(sortedIntervals[i][1])    
        else:
        # sortedIntervals[i][0] < sortedIntervals[i-1][1]:
            numRooms.append(sortedIntervals[i][1])

        numRooms = sorted(numRooms)
        
    return (numRooms)


import heapq

def minMeetingRooms(intervals):
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
    intervals.sort(key= lambda x: x[0])

    # Add the first meeting. We have to give a new room to the first meeting.
    heapq.heappush(free_rooms, intervals[0][1])

    # For all the remaining meeting rooms
    for i in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)

def main():
    intervals1 = [[0,30],[5,10],[15,20]]
    intervals2 = [[7,10],[2,4]]
    intervals3 = [[2,11],[6,16],[11,16], [19,26], [25,27], [20,24] ]
    # [ [ 6,8 ]]
    # print("intervals1--> ",canAttendMeetings(intervals1))
    # print("intervals2--> ",canAttendMeetings(intervals2))

    # [ [2,4], [7,10] ]

    print("intervals1--> ",minMeetingRooms(intervals1))
    print("intervals2--> ",minMeetingRooms(intervals2))
    print("intervals3--> ",minMeetingRooms(intervals3))

    print("leetcode solution--> ", minMeetingRooms(intervals3))
    return 0 

main()