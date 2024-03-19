class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # create a dummy node
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # if there are remaining nodes in either list
    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next

# create first linked list: 1->2->4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# create second linked list: 1->3->4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# merge two lists
merged_list = mergeTwoLists(list1, list2)

# print merged linked list
while merged_list:
    print(merged_list.val, end="->")
    merged_list = merged_list.next
print("None")