class UnionFind: # Reflexive, Symmetric & Transitive
    def __init__(self,objects):
        self.objects = objects
        self.connections = {}
    def union(self,a,b):
        if a in self.connections and b in self.connections:
            self.connections[a].append(b)
            self.connections[b].append(a)
        else:
            self.connections[a] = [b]
            self.connections[b] = [a]
    def showConn(self):
        print('All Connections So Far Made Between The Nodes')
        for node in self.connections:
            print(f'{node}:{self.connections[node]}')

objects = [0,1,2,3,4]
UF_Api = UnionFind(objects)
UF_Api.union(0,1)
UF_Api.union(0,2)
UF_Api.union(0,4)
UF_Api.union(1,2)
UF_Api.union(1,4)
UF_Api.union(2,3)
UF_Api.union(2,4)
UF_Api.showConn()