objects = [0,1,2,3,4]

class QuickFind:
    def __init__(self,objects):
        self.objects = objects
        self.id_array = []
        self.iteration_counter = 0
        for obj in self.objects:
            self.id_array.append(obj)
        print(f'Initial Id Array: {self.id_array}')
    
    def union(self,a,b):
        prev_id_min = min(self.id_array[a],self.id_array[b])
        id_min = min(a,b,prev_id_min)
        for id in range(len(self.id_array)):
            if self.id_array[id] == self.id_array[a] or self.id_array[id] == self.id_array[b]:
                self.id_array[id] = id_min

        self.iteration_counter += 1
        print(f'ID Array (Present -> Iteration {self.iteration_counter}): {self.id_array}')
    
    def findConn(self,a,b):
        if self.id_array[a] == self.id_array[b]:
            print('Connected')
        else:
            print('Not Conn')

# Reivison One-More Time
QF_Api = QuickFind(objects)
QF_Api.union(0,1)
QF_Api.union(3,4)
QF_Api.union(1,4)
QF_Api.findConn(3,4)
QF_Api.findConn(1,2)
