class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        while head:
            temp = ListNode(0)
            temp.next = dummy
            temp = temp.next
        # copy the head to new_Node and add it after where temp stops
            while temp.next and temp.next.val < head.val:
                temp = temp.next
            new_Node = ListNode(head.val)
            # print(temp)
            if temp:
                new_Node.next = temp.next
            temp.next = new_Node
            head = head.next
        return dummy.next