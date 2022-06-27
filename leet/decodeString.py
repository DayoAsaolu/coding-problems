# NOT WORKING
def decodeString(s):
    ans = ""
    stack = []

    for i in s:
        if i != "]":
            stack.append(i)
        else:
            x = ""
            charList = []
            print(stack)
            while len(stack) != 0:
                char = stack.pop()
                if char == "[":
                    n = stack.pop()
                    charList.append(n)+
                    break

                else:
                    charList.append(char)

            text =  "".join(charList[:-1:])
            mulitpy = int(charList[-1])
            x = text*mulitpy

            #   accaccacc
            print("x--:",x)

            print("charList-- ",charList)
            print("ans-- ",ans)
            print("stack-- ",stack)
            print()
            
            


    print(charList)

    return ans


def main():
    # s = "3[a]2[bc]"
    # s = "3[ac]"
    s = "3[a2[c]]"
    #   accaccacc
    print(decodeString(s))
    return 0

main()