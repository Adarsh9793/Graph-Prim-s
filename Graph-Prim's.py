from queue import PriorityQueue 

adjmatrix = [[0,4,5,0] , [4,0,1,3] , [5,1,0,2] , [0,3,2,0]]

def Mst(adjMatrix):
    src = 2
    nodes = PriorityQueue()
    vis = dict()
    nodes.put((0,[src , -1]))  # (cost , node)
    ans = 0
    edges = []

    while nodes.empty() == False:
        (currWeight , temp) = nodes.get()
        currNode = temp[0]
        currParent = temp[1]

        if currNode not in vis:
            vis[currNode] = 1
            if currParent != -1:
                ans += currWeight
                edges.append((currParent , currNode))
           
         

        for i in range(len(adjMatrix)):
            if adjMatrix[currNode - 1][i] > 0 and vis.get(i + 1) != 1:
                nodes.put((adjMatrix[currNode - 1][i] , [i + 1 , currNode]))

    print("Edges: ",edges)

    return ans

print(Mst(adjmatrix))

