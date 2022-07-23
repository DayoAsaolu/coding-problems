from mergeTwoLists import ListNode


def hasCycle(l):
    nodes = {}
    
    while head:
        if head not in nodes:
            nodes[head] = None
        else:
            return True
        head = head.next
    return False


def main():
    
    return 0

main()