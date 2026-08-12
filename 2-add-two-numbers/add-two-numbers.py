# # Definition for singly-linked list (provided by LeetCode)
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to act as the head of the new list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Loop while there are digits left in l1 or l2, OR a carry to process
        while l1 or l2 or carry:
            # Extract values, defaulting to 0 if a list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total = val1 + val2 + carry
            carry = total // 10       # Extract the carry (e.g., 14 // 10 = 1)
            digit = total % 10        # Extract the single digit (e.g., 14 % 10 = 4)
            
            # Append the new digit to our resulting list
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Advance the input pointers if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
