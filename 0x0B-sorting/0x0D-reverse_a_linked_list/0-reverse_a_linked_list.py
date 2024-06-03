class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

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

# Helper function to convert aa linked list to a list of values
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Create a linked list for testing
values = [0,1,2,3]
head = create_linked_list(values)

# Create instance of Solution and reverse the linked list
sol = Solution()
reversed_head = sol.reverseLinkedList(head)

# Convert the reversed linked list back to a list and print the result
reversed_values = linked_list_to_list(reversed_head)
print(reversed_values) # output: [3,2,1,0]
