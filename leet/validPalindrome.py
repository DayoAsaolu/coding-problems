def fasterValidator(s):
    if s == s[::-1]:
        return True
    
    l,r = 0, len(s)-1

    while l < r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            if s[l+1:r+1] == s[l+1:r+1][::-1]:
                return True
            elif s[l:r] == s[l:r][::-1]:
                return True
            else:
                return False
        

def validPalindrome(s):
    l,r = 0, len(s) -1
    removed = 0
    reverStr = s[-1::-1]
    removedRev = 0

    while l < r and removed < 3:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            removed+=1
            r-=1

    l,r = 0, len(s) -1
    while l < r and removedRev < 3:
        if reverStr[l] == reverStr[r]:
            l+=1
            r-=1
        else:
            removedRev+=1
            r-=1
        

    print("removed -->",removed)
    print("removedRev -->",removedRev)
    if removed >= 2 and removedRev >= 2:
        return False
    else:
        return True

def main():
    s = "aba"
    s1 = "acbba"

    print("valid -> ", validPalindrome(s))
    print("---------------------")
    print("valid1 -> ", validPalindrome(s1))
    print("---------------------")
    print("valid_faster -> ", fasterValidator(s1))
    return 0 

main()