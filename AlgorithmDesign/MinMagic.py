# python 3.5.2
import heapq


#
# @param Integer src
# @param Integer dest
# @param Array[][] wizards
# @return Array[Integer, Array[]] [Min Cost, Array Min Path]
#

# class Graph(object):
#     def __init__(self, edge_list):
#         self.edge_list = edge_list
#
#     def add_edge(self, edge_list):
#         self.edge_list.append(edge_list)
#
#     def adj_mtx(self):
#         v = 0
#         counter = set()
#         for src, dest in self.edge_list:
#             counter.add(src)
#             counter.add(dest)
#
#         v = len(counter)
#
#         mtx = [[0 for y in range(v)]for x in range(v)]
#         for e in self.edge_list:
#             src, dest = e
#             src = src - 1
#             dest = dest - 1
#             mtx[src][dest] = 1
#
#         return mtx
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.V_org = vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        if w == 1:
            self.graph[u].append(v)
        else:
            '''split all edges of weight 2 into two 
            edges of weight 1 each.  The intermediate 
            vertex number is maximum vertex number + 1, 
            that is V.'''
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.V = self.V + 1

    # To print the shortest path stored in parent[]
    def printPath(self, parent, j):
        Path_len = 1
        if parent[j] == -1 and j < self.V_org:  # Base Case : If j is source
            print
            j,
            return 0  # when parent[-1] then path length = 0
        l = self.printPath(parent, parent[j])

        # incerement path length
        Path_len = l + Path_len

        # print node only if its less than original node length.
        # i.e do not print any new node that has been added later
        if j < self.V_org:
            print
            j,

        return Path_len

    '''    This function mainly does BFS and prints the 
       shortest path from src to dest. It is assumed 
       that weight of every edge is 1'''

    def findShortestPath(self, src, dest):

        # Mark all the vertices as not visited
        # Initialize parent[] and visited[]
        visited = [False] * (self.V)
        parent = [-1] * (self.V)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(src)
        visited[src] = True

        while queue:

            # Dequeue a vertex from queue
            s = queue.pop(0)

            # if s = dest then print the path and return
            if s == dest:
                return self.printPath(parent, s)

                # Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = s


def getMinMagic(src, dst, wizards):
    minCost = 0
    minPath = []
    # Put your code here to calculate minCost and minPath

    graph = Graph(len(wizards))


    for row in wizards:
        a = b = c = 0
        for i in range(0, len(row)):
            if i == 0: a = row[i]
            elif i == 1: b = row[i]
            else: c = row[i]

        graph.addEdge(a, b, c)

    print("Shortest Path between %d and %d is  " % (src, dst)),
    l = graph.findShortestPath(src, dst)
    print("\nShortest Distance between %d and %d is %d " % (src, dst, l)),

    # Return the result, do not change the structure
    return minCost, minPath



def get_matrix():
    row = 10
    grid = [[] for y in range(row)]

    for i in range(row):
        line = inp[i+2]
        grid[i] = [int(x) for x in list(line)]

    return grid


if __name__ == "__main__":
    inp = ["0", "9", "123", "864", "783", "81", "6", "87", "94", "46", "1", "14"]
    src = int(inp[0]) + 1
    dest = int(inp[1])

    matrix = get_matrix()
    minCost, minPath = getMinMagic(src, dest, matrix)
    result = str(minCost) + " " + "".join([str(elem) for elem in minPath])
    print(result)