import math 

def sumhourglass(i, j, arr):

    top = sum(arr[i][j:j+3])
    mid = arr[i+1][j+1]
    end = sum(arr[i+2][j:j+3])
    return top+mid+end
    
def hourglassSum(arr):
    Max = -math.inf


    hourglass = 1
    for i in range(4):
        for j in range(4):
            # tempMax = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]\
            #     + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
            tempMax = sumhourglass(i,j,arr)
            print("hourGlass number- (%d) -> %d" % (hourglass, tempMax))
            hourglass += 1
            if tempMax > Max:
                Max = tempMax
                
    return Max


def main():
    arr1 = [[-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9,  1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0,  1, 2, 4, 0]]

    arr = [ [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]


    print(hourglassSum(arr1))

    return 0


main()