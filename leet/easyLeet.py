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
                

def main():

    return 0

main()