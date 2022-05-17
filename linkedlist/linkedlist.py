from os import link


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


    def __str__(self):
        return "[" + str(self.data) + "]" + "-> " + str(self.next)

class linkedlist:
    def __init__(self):
        self.headVal = None

    def __str__(self):
        return str(self.headVal)



    # def delDuplicate(self):
    #     current = self.headVal
    #     # This is require to keep track of the prev Node
    #     prev = None
    #     duplicate_dict = dict()
    #     i = 1
    #     print("current ", current)
    #     print("prev ", prev)
    #     print("headVal ", self.headVal,"\n")
        
    #     while current:
    #         print("loop ", i)
    #         if current.data not in duplicate_dict:
    #             duplicate_dict[current.data] = None
    #             # Track the prev Node
    #             prev = current
    #         else:
    #             # When a duplicate is found assign prev Node's next to current's next
    #             prev.next = current.next

    #         current = current.next
    #         print("current ", current)
    #         print("prev ", prev)
    #         print("headVal ", self.headVal,"\n")
    #         i = i+1

    # using buffer
    def delDupilcate(self):
        l1 = self.headVal
        unquie = []
        # print()
        # print("unquie ", unquie)
        # print("l1 from user input", l1,"\n")
        
        while l1:
            if l1.data in unquie:
                l1.next = l1.next.next
                # print("if block ", l1, "\n")
            else:
                unquie.append(l1.next.data)
                # print("else block ", l1)
            l1 = l1.next
            # print("l1.headVal - .headVale.next", l1)
        print("unquie ", unquie)


def deleteMiddle(n):
    if n == None or n.next == None:
        return False
    else:
        a = n.next
        n.data = a.data
        n.next = a.next
        return True

def main():
    l1 = linkedlist()
    l1.headVal = Node(1)
    a,b,c,d,e = Node(2), Node(3), Node(4), Node(5), Node(6)
    l1.headVal.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
   
    print(l1)
    deleteMiddle(b)
    print(l1)
    
    x,y,z = Node(1), Node(1), Node(2)
    l2 = linkedlist()
    l2.headVal = x
    x.next = y
    y.next = z

    r = Node(12)
    s = Node (13)
    t = Node (16)
    z = linkedlist()
    z.headVal = r
    r.next = s
    s.next = t
    
    
    return 0

main()