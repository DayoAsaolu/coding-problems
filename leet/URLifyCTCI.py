def urlify(s,l):
    arr = s.rstrip().split(" ")
    return "%20".join(arr)

def main():
    s = "Mr John Smith    "
    print(urlify(s,13))
    return 0 

main()