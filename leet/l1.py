# 329, 551
class Logger:
    def __init__(self):
        self.loggerRecord = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.loggerRecord:
            if self.loggerRecord[message] <= timestamp:
                self.loggerRecord[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.loggerRecord[message] = timestamp + 10
            return True

def checkRecord(self, s: str) -> bool:
    countA, countL = 0, 0
    
    for r in s:
        if r == "A":
            countA+=1
            countL = 0
        if r == "L":
            countL += 1
        if r == "P":
            countL = 0
        if countA >= 2: return False
        if countL >= 3: return False
        
    return True
                
def isValid(s) -> bool:
        if len(s) % 2 == 1:
            return False
        
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack

def parethesis_validator(test):
    pair_list = ["()", "[]", "{}"]
    parenthesis = ['(', ')', '[', ']', '{', '}']

    test_list = list(test)
    all_parenthesis = True
    for each in test_list:
        if each not in parenthesis:
            all_parenthesis = False
            break
    if not all_parenthesis:
        is_valid = "Error: Please ensure your input is only combination of parentheses. Note: no space or comma need"

    elif len(test) % 2 != 0:  # the count has to be even for it to be in pair
        is_valid = False
    else:
        for i in range(len(test_list)-1):
            pair = test_list[i]+test_list[i+1]
            if pair == pair_list[0] or pair == pair_list[1] or pair == pair_list[2]:  # valid pair
                # save the items, since they would be first removed from the parent list
                pair_item1 = test_list[i]
                pair_item2 = test_list[i+1]

                test_list.pop(i+1)
                test_list.pop(i)  # pop out this items
                # re-insert them in the rigth patter, the closing first and then the opening parethesis
                test_list.insert(0, pair_item2)
                test_list.insert(0, pair_item1)
                # explanation: this way, since u added two, the previous one that failed before would move to the position of i+1 and be rechecked
                # e.g. [()], at i = 0, '[' will fail, but at i=1 '(' will pass, both it, and its opening will move to the front, and at i=2, '[' will be checked again

        is_valid = False
        for i in range(0, len(test_list), 2):
            pair2 = test_list[i]+test_list[i+1]
            # the test is all all ordered now, if any case of unpair was found, the parenthesis failed
            if pair2 != pair_list[0] and pair2 != pair_list[1] and pair2 != pair_list[2]:
                is_valid = False
                break
            else:
                is_valid = True
    return is_valid


def main():
    s = "()[]{}"
    print(isValid(s))
    return 0

main()