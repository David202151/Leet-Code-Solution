class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
            
        
        
                
# --- Funciones helper ---
def to_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# --- Pruebas ---
sol = Solution()

l1 = to_linked_list([2, 4, 3])
l2 = to_linked_list([5, 6, 4])
print(to_list(sol.addTwoNumbers(l1, l2)))

        