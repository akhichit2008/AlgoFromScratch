objects = [0,1,2,3,4]


class WeightedQuickUnion:
    def __init__(self,objects):
        self.objects = objects
        self.sizes = {}
        self.id_array = []
        for obj in self.objects:
            self.id_array.append(obj)
            self.sizes[obj] = 1
        print(f'Initial ID Array : {self.id_array}')
        # self.id_array = [0,1,1,8,3,0,5,1,8,8] # Temporary Testing/Debugging id array
        self.u_count = 0
        print(f'Initial Sizes Array: {self.sizes}')
    
    def findRoot(self,node):
        curr_id = self.id_array[node]
        flag = True
        while flag:
            new_id = self.id_array[curr_id]
            if curr_id == new_id:
               flag = False
               return curr_id
            curr_id = new_id 
        
    def union(self,a,b):
        root_a = self.findRoot(a)
        root_b = self.findRoot(b)
        size_a = self.sizes[root_a]
        size_b = self.sizes[root_b]
        self.u_count += 1
        if root_a == root_b:
            return
        if size_a > size_b:
            self.sizes[root_a] = size_a + size_b
            self.sizes.pop(root_b)
            self.id_array[root_b] = root_a
        elif size_b > size_a:
            self.sizes[root_b] = size_a + size_b
            self.sizes.pop(root_a)
            self.id_array[root_a] = root_b
        else:
            max_root = max(root_b,root_a)
            min_root = min(root_b,root_a)
            self.sizes[max_root] = size_a + size_b
            self.id_array[min_root] = max_root
            self.sizes.pop(min_root)
        print(f'Current ID Array (Union - {self.u_count}):- {self.id_array}')
        #print(f'Current Size Array (Union- {self.u_count}):- {self.sizes}')

WeightedQU_Api = WeightedQuickUnion(objects)
WeightedQU_Api.union(4,3)
WeightedQU_Api.union(3,8)