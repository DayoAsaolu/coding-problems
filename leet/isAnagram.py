def isAnagram(s,t):
    return sorted(s) == sorted(t)

def isAnagram2(s,t):
    return sorted(s) == sorted(t)

def main():
    s = "anagram"
    t = "nagaram"

    print("isValid -->",isAnagram(s,t))

    return 0


main()