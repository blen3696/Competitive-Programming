# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self,node):
        curr = node
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1 = self.reverse(l1)
        list2 = self.reverse(l2)

        res = []
        while list1:
            res.append(list1.val)
            list1 = list1.next
        res2 = []
        while list2:
            res2.append(list2.val)
            list2 = list2.next
        

        my_int = int("".join(map(str, res)))
        my_int2 = int("".join(map(str, res2)))

        my_sum = my_int + my_int2

        digi = [int(digit) for digit in str(my_sum)]

        head = ListNode(digi[0])
        curr = head

        for i in range(1,len(digi)):
            node = ListNode(digi[i])
            curr.next = node
            curr = node

        return self.reverse(head)


        


        

