#delete duplicates from sorted linked list
# temp = head
#         if(temp==None):
#             return
#         while(temp.next!=None):
#             if(temp.val==temp.next.val):
#                 new= temp.next.next
#                 temp.next=new
#             else:
#                 temp = temp.next
#         return head

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __int__(self):
        self.head =None

    def reverse(self):
        next=prev= None
        curr = self.head
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # print(self.printreverse(prev))
        return prev

    def printreverse(self,prev):
        temp = prev
        while(temp!=None):
            print(temp.data)
            temp = temp.next


ll=  LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.reverse()
ll.printreverse(ll.reverse())




