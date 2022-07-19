class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'[{self.val}] --> {self.next}'

def mergeTwoLists(l1, l2):

    return 0

def main():
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))

    print("list1 -->", l1)
    print("List2 -->", l2)

    return 0


main()