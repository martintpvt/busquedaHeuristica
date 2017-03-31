class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}
 
    def neighbors(self, id):
        return self.edges[id]
 
    def cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]
 
 
def heuristic(id):
    """
    Builds Romania heuristic
    """
    H = {
    'Arad': 366,
    'Zerind': 374,
    'Timisoara': 329,
    'Oradea': 380,
    'Lugoj': 244,
    'Mehadia': 241,
    'Dobreta': 242,
    'Sibiu': 253,
    'Rimnicu': 193,
    'Craiova': 160,
    'Fagaras': 176,
    'Pitesi': 100,
    'Bucarest': 0
    }
 
    return H[id]
 
 
def pathfromOrigin(origin, n, parents):
    if origin == n:
        return []
 
    pathO = [n]
    i = n
 
    while True:
        i = parents[i]
        pathO.insert(0, i)
        if i == origin:
            return pathO
 
 
def getF(oL):
    return [i[1] for i in oL]
 
 
def findleastF(oL):
    """
    finds the node with least f in oL
    """
    mF = min(getF(oL))
    for ni in xrange(len(oL)):
        if oL[ni][1] == mF:
            return oL.pop(ni)[0]
 
 
def aStar(graph, start, goal):
    openL = []
    openL.append((start, 0))
    parents = {}
    costSoFar = {}
    parents[start] = None
    costSoFar[start] = 0
     
    while bool(len(openL)):
        current = findleastF(openL)
         
        if current == goal:
            break
         
        for successor in graph.neighbors(current):
            newCost = costSoFar[current] + graph.cost(current, successor)
            if successor not in costSoFar or newCost < costSoFar[successor]:
                costSoFar[successor] = newCost
                priority = newCost
                # priority = newCost + heuristic(successor)
                openL.append((successor, priority))
                parents[successor] = current
    
    print(costSoFar[goal])
    return parents
 
 
def main(argv):
    """
    Usage:
      python aStarRomania.py <startCity>
      Final city will always be Bucarest
      <startCity>:  Any city from
      Arad
      Zerind
      Timisoara
      Oradea
      Lugoj
      Mehadia
      Dobreta
      Sibiu
      Rimnicu
      Craiova
      Fagaras
      Pitesi
                   
    Example:
      python aStarRomania.py Timisoara
    """
    if len(argv) != 2:
        print (main.__doc__)
    else:
        startCity = argv[0]

 
        # Always Bucarest due to heuristic is given for this end city
        endCity = argv[1]
 
        Romania = Graph()  # Builds Romania Graph
 
        # Adding edges (adjacency list)
        Romania.edges = {
            'O': ['A', 'B', 'C'],
            'A': ['O', 'B', 'D'],
            'B': ['O', 'A', 'C', 'D'],
            'C': ['O', 'B', 'E'],
            'D': ['A', 'B', 'E', 'T'],
            'E': ['C', 'D', 'T'],
            'T': ['D', 'E']
        }
        # Adding weights to edges
        Romania.weights = {
            ('O', 'A') : 2, ('O', 'B') : 5, ('O', 'C') : 4,
            ('A', 'O') : 2, ('A', 'B') : 2,('A', 'D') : 7,
            ('B', 'O') : 5, ('B', 'A') : 2,('B', 'C') : 1,('B', 'D') : 4,('B', 'E') : 3,
            ('C', 'O') : 4,('C', 'B') : 1,('C', 'E') : 4,
            ('D', 'A') : 7,('D', 'B') : 4,('D', 'E') : 1,('D', 'T') : 5,
            ('E', 'C') : 4,('E', 'D') : 1,('E', 'T') : 7,
            ('T', 'D') : 5,('T', 'E') : 7
        }
 
        if argv[0] not in Romania.edges.keys() or argv[1] not in Romania.edges.keys():
            print ("Ciudad no existe")
            return
 
        # Building aStar path of parents
        parents = aStar(Romania, startCity, endCity)
 
        # Printing the path
        print (pathfromOrigin(startCity, endCity, parents))
         
 
 
if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
