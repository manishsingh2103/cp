class graph :
    def __init__(self) :
        self.adj_list={}

    def add_edge(self,start,end):
        if start not in self.adj_list :
            self.adj_list[start]=[end]
        else :
            if end not in  self.adj_list[start] :
                self.adj_list[start].append(end)

        if end not in self.adj_list :
            self.adj_list[end]=[start]
        else :
            if start not in self.adj_list[end]:
                self.adj_list[end].append(start)

    def bfs(self,start):
        visited={}
        level={}
        parent={}
        bfs_op = []
        q=[]

        for node in self.adj_list.keys() :
            visited[node]=False
            level[node]=-1
            parent[node]=None

        level[start]=0
        visited[start]=True
        q.append(start)

        while len(q) > 0 :
            node=q.pop(0)
            bfs_op.append(node)
            for i in self.adj_list[node] :
                if visited[i] == False :
                    visited[i]=True
                    level[i]+=1
                    parent[i]=node
                    q.append(i)

        print(bfs_op)

    def dfs(self, start):
            visited = {}
            level = {}
            parent = {}
            dfs_op = []
            q = []

            for node in self.adj_list.keys():
                visited[node] = False
                level[node] = -1
                parent[node] = None

            level[start] = 0
            visited[start] = True
            q.append(start)

            while len(q) > 0:
                node = q.pop(-1)
                dfs_op.append(node)
                for i in self.adj_list[node]:
                    if visited[i] == False:
                        visited[i] = True
                        level[i] += 1
                        parent[i] = node
                        q.append(i)

            print(dfs_op)


if  __name__ == '__main__' :
    root=graph()
    root.add_edge(1,2)
    root.add_edge(1,4)
    root.add_edge(2,3)
    root.add_edge(1,2)
    root.add_edge(4,5)
    root.add_edge(4,6)
    root.add_edge(5,6)
    root.add_edge(5,7)
    root.add_edge(7,8)
    root.add_edge(6,8)
    print(root.adj_list)

    root.dfs(1)