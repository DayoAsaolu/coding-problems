def groupAnagrams(strs):
    anagrams = {}
    
    for w in strs:
        s = "".join(sorted(w))
        if s not in anagrams:
            anagrams[s] = [w]
        else:
            anagrams[s].append(w)
            
    ans = []
    for i in anagrams:
        ans.append(anagrams[i])
        
    return ans


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = [""]
    print("anagrams list ->", groupAnagrams(strs))
    return 0

main()
