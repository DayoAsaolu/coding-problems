def uniqueString(str):
    arr = [False] * 128
    for char in str:
        index = ord(char)
        if arr[index]:
            return False
        arr[index] = True

    return True


def main():
    for i in range(1):
        print(str(i), uniqueString("apple"))
        print(str(i+1), uniqueString("algorithm"))
        print(str(i+2), uniqueString("software"))
        print(str(i+3), uniqueString("machineLearning"))
    return 0

main()