# not working
def longestPalindrome(s):
    if s == s[::-1]:
        return True
    
    l,r = 0, len(s)-1
    z = 1
    while l <= r:
        print("loop--",z)
        if s[l:r+1] == s[l:r+1][::-1]:
            return s[l:r+1]
        else:
            if s[l+1:r+1] == s[l+1:r+1][::-1]:
                return s[l+1:r+1]
            elif s[l:r] == s[l:r][::-1]:
                return s[l:r]
            else:
                longestPalindrome(s[l+1:r+1])
                longestPalindrome(s[l:r])
                # l+=1
                # r-=1
        z+=1

    return ""

def main():
    s1 = "babad"
    s2 = "cbbd"
    s3 = "eabcb"
    
    print("longest --> ",longestPalindrome(s1))
    print("longest --> ",longestPalindrome(s2))
    print("longest --> ",longestPalindrome(s3))
    return 0

main()