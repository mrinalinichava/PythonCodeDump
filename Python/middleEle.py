class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __int__(self):
        self.head = None

    def middle(self):
        slow=fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def reverse(self):
        prev= None
        next ,curr= None,self.head
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev=curr
            curr=next
        self.head = prev
        # temp = self.head
        # while(temp!=None):
        #     print(temp.data)
        #     temp = temp.next
        printLL()
        return self.head

    def printLL(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    def rotate(self,k):
        if(k==0):
            return 

        curr = self.head
        count = 1
        while(count<k and curr!=None):
            curr=curr.next
            count=count+1
        if(curr is None):
            return
        kNode = curr
        while(curr.next!=None):
            curr=curr.next
        curr.next = self.head
        self.head = kNode.next
        kNode.next = None
                




node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
ll = LinkedList()
ll.head = node
ll.rotate(2)
ll.printLL()

# print(ll.middle())
# # print(ll.reverse(node))
# print(ll.reverse().data)
# ll.reverse()
# ll.printLL()
