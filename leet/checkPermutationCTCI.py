def sortAndcompare(s1,s2):
    if len(s1) != len(s2): return False
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))
    return s1==s2

def convASCIIAndcompare(s1,s2):
    if len(s1) != len(s2): return False

    #Assumption ASCII
    arr = [0] * 128
    
    # apple , pplea
    # [..1...2..1...1] -- [..0...0..0...0]

    # anl , all
    # [..1...2..1...1] -- [..0...1..0..0..1]
    for char in s1:
        index = ord(char)
        arr[index] += 1

    for char in s2:
        index = ord(char)
        arr[index] -= 1
        if arr[index] < 0: return False

    return True

    
def main():
    s1 = "apple"
    s2 = "elppa"
    s3 = "alphabeth"
    s4 = "pysccicuu"
    s5 = "waterloo"

    print(sortAndcompare(s1,s2))
    print(sortAndcompare(s3,s4))
    print(convASCIIAndcompare(s1,s2))
    print(convASCIIAndcompare(s4,s5))
    
    return 0
    
main()