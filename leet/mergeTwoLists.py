class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'[{self.val}] --> {self.next}'

def mergeTwoLists(l1, l2):
    prehead = ListNode()
    head = prehead
    
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        
        head = head.next
        
    
    if l1:
        head.next = l1
    elif l2:
        head.next = l2
        
    return prehead.next
    

def main():
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))

    print("list1 -->", l1)
    print("List2 -->", l2)
    print("merged l1 and l2 -->", mergeTwoLists(l1,l2))

    return 0

if __name__ == "__main__":
    main()