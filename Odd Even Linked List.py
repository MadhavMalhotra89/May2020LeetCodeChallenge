if head == None:
            return None
        odd = head
        even = head.next
        evenhead =  even
        while even != None and even.next != None:
            odd.next =  even.next
            odd  = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
