def convert(s, numRows):
    direction = -1
    row = 0
    res = [[] for i in range(numRows)]
    
    for c in s:
        # print(c)
        res[row].append(c)
        if row == 0 or row == numRows -1:
            direction *= -1
        row+= direction

    print(res)
    for i in range(len(res)):
        res[i]= ''.join(res[i])

    return ''.join(res)

def main():
    print(convert("PAYPALISHIRING", 4))
    return 0


main()
