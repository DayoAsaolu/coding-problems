def maxProfit(prices):
    buy, sell = prices[0], prices[0]
    calprofit = 0
    
    for i in prices[1:]:
        if buy > i:
            buy = i
            sell = i
        else:
            sell = i
        
        tempProfit = sell - buy
        calprofit = max(calprofit, tempProfit)
        
    
    return calprofit

def main():
    prices1 = [7,6,4,3,1]
    prices2 = [7,1,5,3,6,4]

    print("cal max Profit -->", maxProfit(prices1))
    print("cal max Profit -->", maxProfit(prices2))

    return 0

main()