objects = [0,1,2,3,4]

class QuickUnion:
    def __init__(self,objects):
        self.objects = objects
        self.id_array = []
        for obj in self.objects:
            self.id_array.append(obj)
        print(f'Initial ID Array : {self.id_array}')
        # self.id_array = [0,1,1,8,3,0,5,1,8,8] # Temporary Testing/Debugging id array
        self.u_count = 0
    
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
        self.id_array[root_a] = root_b
        self.u_count += 1
        print(f'Current ID Array (Union - {self.u_count}):- {self.id_array}')
    
    def find(self,a,b):
        root_a = self.findRoot(a)
        root_b = self.findRoot(b)
        if root_a == root_b:
            print('Connected Objects')
        else:
            print('Not Connected Objects')

QU_Api = QuickUnion(objects)
QU_Api.union(4,3)
QU_Api.union(3,8)
QU_Api.union(6,5)
QU_Api.union(9,4)
QU_Api.union(2,1)
QU_Api.union(5,0)
QU_Api.union(7,2)
QU_Api.union(6,1)
QU_Api.find(6,7)
QU_Api.find(6,8)