# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st =[]
        a=head
        while a:
            st.append(a.val)
            a = a.next
        a = head
        while a:
            if st.pop()!=a.val:
                return False
            a = a.next
        return True

        