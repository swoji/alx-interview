class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Create a linked list for testing
values = [0, 1, 2, 3]
head = create_linked_list(values)

# Create instance of Solution and reverse the linked list
sol = Solution()
reversed_head = sol.reverseList(head)

# Convert the reversed linked list back to a list and print the result
reversed_values = linked_list_to_list(reversed_head)
print(reversed_values)  # Expected output: [3, 2, 1, 0]

