    
def reorderSpace(text):
    countSpace = 0
    for c in text:
        if c == " ":
            countSpace += 1
            
    words = []
    w = ""
    for c in text:
        if c == " ":
            if len(w) > 0 :
                words.append(w)
            w = ""
        else:
            w+=c
    if len(w) > 0 :words.append(w)
    if len(words) == 1: return words[0] + " "* countSpace
            
    textReturn = ""
    aveSpace = countSpace // (len(words) -1)
    remSpace = countSpace % (len(words) -1)

    
    for i in range(len(words) -1):
        space = " " * aveSpace
        textReturn  += words[i] + space
        
    textReturn += words[-1] + " " * remSpace
    
    return textReturn


def main():
    text = "this   is   a   sentence"
    print(reorderSpace(text))
    return 0


main()