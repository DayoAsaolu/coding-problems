def generateRings():
    r = dict()

    for i in range(10):
        r[i] = set()

    return r

def countPoints(rings) -> int:
    rods = {i:set() for i in range(10)}
    # rods = generateRings()
    
    for i in range(0, len(rings), 2):
        col, pos = rings[i], int(rings[i+1])
        rods[pos].add(col)
            
            
    allcol = 0
    print(rods)
    for i in range(len(rods)):
        if len(rods[i]) == 3:
            allcol += 1
            
    return allcol


def main():
    s = "B0B6G0R6R0R6G9"


    print(countPoints(s))
    return 0


main()

