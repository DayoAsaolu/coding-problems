from operator import imod


import math

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    
    L = len(s)
    rows, cols = math.floor(L), math.ceil(L)
    result = ""
    
    print("sss->",s,"--",L,"--",rows,"--",cols)
    # for i in range(cols):
    #     for j in range(i, rows*cols, cols):
    #         result += s[j]
            
    return result


def main():
    s = "haveaniceday"
    print(encryption(s))
    return 0


main()