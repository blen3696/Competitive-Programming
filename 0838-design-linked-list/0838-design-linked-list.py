class ListNode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head 
        ctn = 0
        while curr:
            if ctn == index:
                return curr.val
           
            curr = curr.next
            ctn += 1
        return -1
 

    def addAtHead(self, val: int) -> None:
        Node = ListNode(val)
        Node.next = self.head
        self.head = Node
        

    def addAtTail(self, val: int) -> None:
        Node = ListNode(val)

        if not self.head:
            self.head = Node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node
    

    def addAtIndex(self, index: int, val: int) -> None:
        Node = ListNode(val)

        if index == 0:
            self.addAtHead(val)
            return

        ctn = 0
        curr = self.head
        while curr and  ctn < index - 1:
                curr = curr.next
                ctn +=1
        if not curr:
            return 
            
        Node.next = curr.next
        curr.next = Node

    def deleteAtIndex(self, index: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        curr = dummy
        ctn = 0

        while curr and curr.next:
            if ctn == index:
                 curr.next = curr.next.next
                 break
            curr = curr.next
            ctn += 1
        self.head = dummy.next
            

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)