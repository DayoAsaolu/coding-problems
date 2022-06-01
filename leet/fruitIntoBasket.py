def fruitsIntoBasket(fruits):
            
        maz = 0
        basket = {}
        
        for pos in range(len(fruits)):
            fruitPos = pos
            temp_max = 0
            basket = {}
            print("pos--", pos)
            while len(basket) <= 2 and fruitPos < len(fruits):
                print("fruitPos--", fruitPos)
                fruitType = fruits[fruitPos]
                if fruitType not in basket and len(basket) < 2:
                    basket[fruitType] = 1
                    temp_max += 1
                    
                elif fruitType in basket:
                    basket[fruitType] += 1
                    temp_max += 1
                    
                else:
                    break
                    
            
                fruitPos += 1
            if temp_max > maz: maz = temp_max
                
                
        return maz



def main():
    fruits = [0, 1, 2, 2]

    print(fruitsIntoBasket(fruits))
    return 0

main()