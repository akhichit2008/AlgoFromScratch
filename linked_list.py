class LinkedList:
    def __init__(self,r_node):
        self.r_node = r_node

    def DisplayLinkedList(self):
        curr_node = self.r_node
        l_node = False
        while l_node != True:
            print(curr_node.value,end=' -> ')
            curr_node = curr_node.next
            if curr_node.is_last == True:
                l_node = True
                print(curr_node.value)

    def AddNewNode(self,value,prev,next):
        node = Node(value,prev=prev,next=next)
    



class Node:
    def __init__(self,value,is_root=False,is_last=False,prev=None,next=None):
        self.prev = prev
        self.next = next
        self.value = value
        self.is_last = is_last
        self.is_root = is_root
        if self.is_last:
            self.next=None
        if self.is_root:
            self.prev=None
    
    def DisplayVal(self):
        print(self.value)

    def AddNext(self,node_next):
        self.next = node_next
    def AddPrev(self,node_previous):
        self.prev = node_previous
    
    def DisplayNextNode(self):
        print(self.next)

    def DisplayPrevNode(self):
        print(self.prev)

r_node = Node(3,is_root=True)
node1 = Node(7,prev=r_node)
node2 = Node(6,prev=node1)
l_node = Node(5,is_last=True,prev=node2)
r_node.next = node1
node1.next = node2
node2.next = l_node
l_prev = node2
list = LinkedList(r_node)
list.DisplayLinkedList()
