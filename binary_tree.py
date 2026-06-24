class BinTree:
    def __init__(self,r_node):
        self.r_node = r_node
    
    def TraverseBinTree(self,t_left=False,t_right=False):
        curr_node = self.r_node
        is_last_node = False
        while is_last_node != True:
            if curr_node.is_root == True:
                print(curr_node.value)
            if curr_node.is_last == False:
                c1_val = curr_node.c1.value
                c2_val = curr_node.c2.value
                print(f'/{c1_val}      \\{c2_val}')
                if t_left == True:
                    curr_node = curr_node.c1
                if t_right == True:
                    curr_node = curr_node.c2
            
            else:
                is_last_node = True
                break

class Node:
    def __init__(self,value,c1=None,c2=None,is_root=False,is_last=False):
        self.is_root = is_root
        self.value = value
        self.c1 = c1
        self.c2 = c2
        self.is_last = is_last

r_node = Node(4,is_root=True)
c1_node = Node(5,is_last=True)
c2_node = Node(7,is_last=True)
r_node.c1 = c1_node
r_node.c2 = c2_node

bin_tree = BinTree(r_node)
bin_tree.TraverseBinTree(t_left=True,t_right=False)