# list comprehension with if,else statement, for loop
# https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals

def compareTriplet():
    a = [3,2,1]
    b = [1,2,3]
    # [output if condition else output for l in list]
    # ['even' if num%2 == 0 else 'odd' for num in nums]
    
    c = list(zip(a,b))
    # x = [[i,j] if ]
    print(c)
    print(c[0][0])
    # l = [1, 2, 3, 4, 5]
    # ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]
    i,j=0,0 
    x = [ "a" if i[0] > i[1] else "b" if i[0] < i[1] else "c" for i in c]
    print(x)
    return [x.count('a'),x.count('b')]
    

def sumVeryBigInt(arr):
    return sum(arr)

def main():
    # s = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    # # print(compareTriplet())
    # print(sumVeryBigInt(s))

    evenOdd()
    return 0

def evenOdd():
    n = int(input())
    for i in range(n):
        s = input()
    print(" ".join([s[::2],s[1::2]]))
    return 0
    # for i in range(int(input())): 
    #     s=input(); 
    #     print(*["".join(s[::2]),"".join(s[1::2])])

def diagonalDifference(arr):
    # Write your code here
    l = len(arr)
    x,y,k = 0,0,0
    j=l-1
    for i in range(n):
        x+=arr[i][i]
        y+=arr[k][j]
        k+=1
        j-=1
    
    return abs(x-y)

main()