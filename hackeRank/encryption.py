from operator import imod


import math

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    
    L = len(s)
    rows, cols = math.floor(L**(0.5)), math.ceil(L**(0.5))
    if rows * cols < L: 
        rows = cols
    result = ""
    
    print("sss->",s,"--",L,"--",rows,"--",cols)
    for i in range(cols):
        for j in range(i, rows*cols, cols):
            if j < L:
                result += s[j]
            
        result += " "
            
    return result


def main():
    s = "haveaniceday"
    # s = "chillout"
    print(encryption(s))
    return 0


main()