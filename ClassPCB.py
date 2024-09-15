import math
class PCB:
    def __init__(self,N,M):
        self.grid = [[0 for i in range(M)]for j in range(N)]
        self.N=N
        self.M=M
    
    def routesToB(self):
        paths=0
        self.grid[self.N-1][0:self.M-1]=[1 for i in range(0,self.M-1)]
        for i in range(0,self.N-1):
            self.grid[i][self.M-1]=1
        for i in range(self.N-2,0,-1):
            for j in range(self.M-2,0,-1):
                self.grid[i][j] = self.grid[i+1][j] + self.grid[i][j+1]
        for s in self.grid:
            paths+=sum(s)
        return paths
    
    def routesToB2(self):
        paths=1
        for i in range(0,self.N-1):
            for j in range(i,self.M-1+i):
                paths+=math.comb(j,i)
        return paths
    
    def routesToB_S(self,method):
        if(method==1):
            return self.routesToB()
        elif(method==2):
            return self.routesToB2()
        else:
            print(f'El metodo {method} no existe')
            return        

