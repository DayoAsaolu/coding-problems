def licenceKeyFormat(s, k) -> str:
    s = s.replace("-", "")
    s = s.upper()
    s = s[::-1]

    r = ""
    for i in range(0, len(s), k):
        r += s[i:i+k:] + "-"
        
    r = r[:-1:]

    r = r[::-1]

    return r


def main():
    # s, k = "5F3Z-2e-9-w", 4

    s, k = "2-5g-3-J", 2
    print(licenceKeyFormat(s, k))
    return 0


main()