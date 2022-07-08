# half done

def fullJustify(words, m):
    # - each line
    #   - length == m
    #   - maximum amount of words
    #   - left and right justified
    #   - extra spaces should be distributed evenly as possible
    #       - if not possible left should have the most spaces
    #   - last line of text, it should be left-justified, and no extra space is inserted between words.

    # this is an example of text justification
    '''
    [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    '''
    def validatePartition(line, m, z):
        if len(line) -1 + len("".join(line)) <= m:
            # print (f" [{z}] - validate if")
            return True
        else:
            # print (f" [{z}] - validate else")
            False

    refined = []
    words = words[-1::-1]
    line = []
    z = 1
    while len(words) != 0:

        line.append(words.pop())
        # print (f" [{z}]")
        if validatePartition(line, m, z):
            # print (f" [{z}] if block")
            # print("line --> *",line)
            
            # print("line --> #",line)
            pass
        else:
            # print (f" [{z}] else block")
            words.append(line.pop())
            # print("line --> ",line)
            refined.append(line)
            # print("words -> ", words)
            # print("------------------------")
            line = []

        z+=1

    refined = refined + [line]
    print("refined =", refined)

    def addSpaces(refined,m):
        str = ""
        midstr = ""
        endstr = ""
        if len(refined) == 1:
            wordsCount = len(refined[0])
            calSpace = m - len("".join(refined[0]))
            evenSpace = calSpace // wordsCount
            extraSpace = calSpace % wordsCount
            print( f" {wordsCount} -- {calSpace} -- {evenSpace} -- {extraSpace} " )
            temp = (" "*evenSpace).join(refined[0])
            temp += " "*extraSpace + " "*evenSpace
            str += temp

        for line in refined[:-1:]:
            print(line)
            wordsCount = len(line)
            calSpace = m - len("".join(line))
            evenSpace = calSpace // (wordsCount -1)

            check = len(" ".join(line)) + (evenSpace* (wordsCount-1))
            print(check)
            if check == m:
                midstr = midstr + " ".join(line) + ","
            else:
                pass
        # # spaces for the last line
        
        wordsCount = len(refined[-1])
        calSpace = m - len("".join(refined[-1]))
        evenSpace = calSpace // wordsCount
        extraSpace = calSpace % wordsCount
        print( f" {wordsCount} -- {calSpace} -- {evenSpace} -- {extraSpace} " )
        temp = (" "*evenSpace).join(refined[-1])
        temp += " "*extraSpace + " "*evenSpace
        endstr = endstr + temp

        return str+midstr+endstr
    
    # |an axe is blue |

    
    return addSpaces(refined, m)

def main():

    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    words4 = ["an","axe","is","blue"]
    maxWidth4 = 16
    words5 = ["eat","ate","bat","pie","egg","fed","yam","tea"]
    maxWidth5 = 15

    print("jusified: |",fullJustify(words5, maxWidth5) + "|")

    # ["an  axe  is blue","gold            "]

    return 0

main()