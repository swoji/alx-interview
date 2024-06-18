class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def listnode_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Example usage:
list1 = [1, 2, 4]
list2 = [1, 3, 5]

# Convert lists to ListNodes
list1_node = list_to_listnode(list1)
list2_node = list_to_listnode(list2)

# Merge the two ListNodes
sol = Solution()
merged_list_node = sol.mergeTwoLists(list1_node, list2_node)

# Convert the merged ListNode back to a list
merged_list = listnode_to_list(merged_list_node)
print(merged_list)  # Output: [1, 1, 2, 3, 4, 5]
