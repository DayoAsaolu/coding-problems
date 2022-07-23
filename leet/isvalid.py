def isValid(s):
    brackets = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
    }
    
    stack = []
    for i in s:
        if i not in brackets:
            stack.append(i)
        else:
            
            if len(stack) == 0:
                return False
            else:
                prev = stack.pop()
                if brackets[i] != prev:
                    return False
                
    
    if stack: 
        return False
    else:
        return True


def main():
    a = "()[]{}"
    b = "()"
    c = "(]"

    print("isvalid -->", isValid(a))
    print("isvalid -->", isValid(b))
    print("isvalid -->", isValid(c))

    return 0


main()