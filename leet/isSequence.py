def isSubsequence1(s: str, t: str) -> bool:

    if len(s) > len(t): return False
    
    sp, tp = 0, 0
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
            tp += 1
        else:
            tp += 1
    if sp != len(s): return False
    else: return True
    
def isSubsequence2(s: str, t: str) -> bool:

    if len(s) > len(t): return False

    def helper( t, target):
        if target in t:
            pos = t.index(target)
            return (True, t[pos+1::])
        else:
            return (False, "")
        
        
    for i in s:
        check = helper(t, i)
        if not check[0]:
            return False
        
        t = check[1]
        
    return True

def main():
    s, t = "abc", "ahbgdc"
    print(isSubsequence1(s,t))
    return 0

main()