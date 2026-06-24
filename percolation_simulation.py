
import pygame
import warnings

pygame.init()
screen_width = 720
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
warnings.filterwarnings('ignore',category=UserWarning,module='pygame')

shown = False


class Site:
    def __init__(self,coordinates,screen,open,N_gridsize=6):
        self.open = open
        self.coordinates = coordinates
        self.N_gridsize = N_gridsize
        self.x,self.y = coordinates
        self.width_square = screen_width//N_gridsize
        self.height_square = screen_height//N_gridsize
    
    def __repr__(self):
        return f'''Site: 
        Open :- {self.open}
        Coords :- {self.coordinates}
        Dimension - {self.width_square}x{self.height_square}'''
    
    def drawSite(self):
        if self.open:
            pygame.draw.rect(screen,(0,0,255),(self.x,self.y,self.width_square,self.height_square))
            pygame.draw.rect(screen, (255, 255, 255), (self.x,self.y,self.width_square,self.height_square), 5)
        else:
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width_square,self.height_square))
            pygame.draw.rect(screen, (255, 255, 255), (self.x,self.y,self.width_square,self.height_square), 5)

class Grid:
    def __init__(self,grid,dimensions=(),N_gridsize=6):
        self.N_gridsize = N_gridsize
        self.dimensions = dimensions
        self.grid = grid
        self.width_square = screen_width//N_gridsize
        self.height_square = screen_height//N_gridsize
        if not self.dimensions:
            self.dimensions = (screen_width,screen_height)

    def drawGrid(self):
        for i in range(self.N_gridsize):
            for j in range(self.N_gridsize):
                coordinates = (j*self.width_square,i*self.height_square)
                if self.grid[i][j] == 1:
                    si = Site(coordinates,screen,True)
                    si.drawSite()
                else:
                    si = Site(coordinates,screen,False)
                    si.drawSite()


class AppliedQuickUnion:
    def __init__(self,objects):
        self.objects = objects
        self.sizes = {}
        self.id_array = []
        for i in range(len(objects)):
            row = []
            for j in range(len(objects)):
                row.append((i,j))
                self.sizes[(i,j)] = 1
            self.id_array.append(row)
        print(f'Initial ID Array : {self.id_array}')
        # self.id_array = [0,1,1,8,3,0,5,1,8,8] # Temporary Testing/Debugging id array
        self.u_count = 0
        print(f'Initial Sizes Array: {self.sizes}')
    
    def findRoot(self,node_x,node_y):
        if (node_x,node_y) in self.sizes and node_x < 0:
            return (node_x,node_y)
        curr_id = self.id_array[node_x][node_y]

        while True:
            curr_id_x,curr_id_y = curr_id
            if curr_id_x < 0:
                return curr_id
            new_id = self.id_array[curr_id_x][curr_id_y]
            if curr_id == new_id:
                return curr_id
            
            curr_id = new_id


    def union(self,x_a,y_a,x_b,y_b):
        root_a = self.findRoot(x_a,y_a)
        root_b = self.findRoot(x_b,y_b)
        size_a = self.sizes[root_a]
        size_b = self.sizes[root_b]
        self.u_count += 1
        if root_a == root_b:
            return
        if size_a > size_b:
            self.sizes[root_a] = size_a + size_b
            self.sizes.pop(root_b)
            self.id_array[root_b[0]][root_b[1]] = root_a
        elif size_b > size_a:
            self.sizes[root_b] = size_a + size_b
            self.sizes.pop(root_a)
            self.id_array[root_a[0]][root_a[1]] = root_b
        else:
            max_root = max(root_b,root_a)
            min_root = min(root_b,root_a)
            max_root_x,max_root_y = max_root
            min_root_x,min_root_y = min_root
            self.sizes[max_root] = size_a + size_b
            self.id_array[min_root[0]][min_root[1]] = max_root
            self.sizes.pop(min_root)
        print(f'Current ID Array (Union - {self.u_count}):- {self.id_array}')
        #print(f'Current Size Array (Union- {self.u_count}):- {self.sizes}')
    
    def connectSites(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 1:
                    continue
                if i > 0 and grid[i-1][j] == 1:
                    self.union(*(i,j,i-1,j))
                if i < len(grid)-1 and grid[i+1][j] == 1:
                    self.union(*(i,j,i+1,j))
                if j>0 and grid[i][j-1] == 1:
                    self.union(*(i,j-1,i,j))
                if j < len(grid)-1 and grid[i][j+1] == 1:
                    self.union(*(i,j,i,j+1))
        print(f'Current ID Array : {self.id_array}')
    
    def checkPercolation(self,top_site,bottom_site):
        if self.findRoot(*top_site) == self.findRoot(*bottom_site):
            print('Percolates Succesfully')
        else:
            print('Percolates Unsucessfully')

    def createVirtualSite(self,grid):
        top = self.id_array[0]
        bottom = self.id_array[len(self.id_array)-1]
        top_site = (-1,-1)
        bottom_site = (-2,-2)
        self.sizes[top_site] = 1
        self.sizes[bottom_site] = 1
        for node in top:
            if grid[node[0]][node[1]] == 1:
                node_x,node_y = node
                top_x,top_y = top_site
                self.union(*(node_x,node_y,top_x,top_y))
        
        for node in bottom:
            if grid[node[0]][node[1]] == 1:
                node_x,node_y = node
                bottom_x,bottom_y = bottom_site
                self.union(*(node_x,node_y,bottom_x,bottom_y))
            
        print('Created Virtual Nodes Successfully')

        self.checkPercolation(top_site,bottom_site)

grid_outliner = [[0,0,1,0,1,0],[1,0,1,0,1,1],[1,0,1,0,1,1],[0,1,1,0,1,0],[1,0,1,0,1,0],[0,0,1,1,1,0]] # used for testing/debug
QU_Api = AppliedQuickUnion(grid_outliner)
QU_Api.connectSites(grid_outliner)
QU_Api.createVirtualSite(grid_outliner)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    #surface = pygame.Surface(((screen_width,screen_height)))
    screen.fill((255,255,255))
    grid_outliner = [[0,0,0,0,0,0],[1,0,1,0,1,1],[1,0,1,0,1,1],[0,1,1,0,1,0],[1,0,1,0,1,0],[0,0,1,1,1,0]]
    grid = Grid(grid_outliner)
    grid.drawGrid()
    pygame.display.flip()
    clock.tick(60)