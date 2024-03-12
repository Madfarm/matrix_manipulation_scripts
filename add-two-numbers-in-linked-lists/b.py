class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        current.next = ListNode(carry % 10)
        current = current.next
        carry //= 10
    
    return dummy.next

# Example usage
# Create the first list: 243
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create the second list: 564
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Add the two lists
result = addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end='')
    result = result.next
    if result:
        print(' -> ', end='')
print()