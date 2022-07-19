class codec:

    def encode(self, strs):
        s = ""
        delinmiter = "!"

        for i in strs:
            l = len(i)
            s += str(l) + delinmiter + i

        return s

    def decode(self, s):
        strs = []
        i=0
        while i<= len(s)-1:
            j=i
            while s[j].isnumeric():
                j+=1
            
            d = j - i
            l = int(s[i:j])
            w = s[ i+d+1:i+d+1+l ]
            strs.append(w)
            i += d +l +1
            print("str->%s -- l->%s -- w->%s -- i->%d" % (str(strs), l, str(w), i))
        return strs


def main():
    strs = ["HelloTorontoON", "WorldBreak", "right"]

    # strs = ["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]
    Codex = codec()
    encode = Codex.encode(strs)
    print((encode))
    decode = Codex.decode(encode)
    
     
    print("[encode] -- [decode] --> %s  -- %s" % (encode, decode)  )
    return 0


main()