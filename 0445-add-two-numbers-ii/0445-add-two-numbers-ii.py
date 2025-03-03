# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2

        arr1 = []
        arr2 = []

        while list1:
            arr1.append(list1.val)
            list1 = list1.next
        while list2:
            arr2.append(list2.val)
            list2 = list2.next

        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str,arr2)))

        my_sum = num1 + num2
        digits = list(map(int, str(my_sum)))


        dummy = ListNode(0)
        curr = dummy

        for num in digits:
            node = ListNode(num)
            curr.next = node
            curr = node

        return dummy.next
        
        