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
                priority = newCost + heuristic(successor)
                openL.append((successor, priority))
                parents[successor] = current
     
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
    if len(argv) != 1:
        print (main.__doc__)
    else:
        startCity = argv[0]
 
        # Always Bucarest due to heuristic is given for this end city
        endCity = 'Bucarest'
 
        Romania = Graph()  # Builds Romania Graph
 
        # Adding edges (adjacency list)
        Romania.edges = {
            'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
            'Zerind': ['Arad', 'Oradea'],
            'Timisoara': ['Arad', 'Lugoj'],
            'Oradea': ['Zerind', 'Sibiu'],
            'Lugoj': ['Timisoara', 'Mehadia'],
            'Mehadia': ['Lugoj', 'Dobreta'],
            'Dobreta': ['Mehadia', 'Craiova'],
            'Sibiu': ['Arad', 'Oradea', 'Rimnicu', 'Fagaras'],
            'Rimnicu': ['Sibiu', 'Craiova', 'Pitesi'],
            'Craiova': ['Dobreta', 'Rimnicu', 'Pitesi'],
            'Fagaras': ['Sibiu', 'Bucarest'],
            'Pitesi': ['Rimnicu', 'Craiova', 'Bucarest'],
            'Bucarest': ['Fagaras', 'Pitesi']
        }
 
        # Adding weights to edges
        Romania.weights = {
            ('Arad', 'Zerind') : 75, ('Arad', 'Timisoara') : 118, ('Arad', 'Sibiu') : 140,
            ('Zerind', 'Arad') : 75, ('Zerind', 'Oradea') : 71,
            ('Timisoara', 'Arad') : 118, ('Timisoara', 'Lugoj') : 111,
            ('Oradea', 'Zerind') : 71, ('Oradea', 'Sibiu') : 151,
            ('Lugoj', 'Timisoara') : 111, ('Lugoj', 'Mehadia') : 70,
            ('Mehadia', 'Lugoj') : 70, ('Mehadia', 'Dobreta') : 75,
            ('Dobreta', 'Mehadia') : 75, ('Dobreta', 'Craiova') : 120,
            ('Sibiu', 'Arad') : 140, ('Sibiu', 'Oradea') : 151, ('Sibiu', 'Rimnicu') : 80, ('Sibiu', 'Fagaras') : 99,
            ('Rimnicu', 'Sibiu') : 80, ('Rimnicu', 'Craiova') : 146, ('Rimnicu', 'Pitesi') : 97,
            ('Craiova', 'Dobreta') : 120, ('Craiova', 'Rimnicu') : 146, ('Craiova', 'Pitesi') : 138,
            ('Fagaras', 'Sibiu') : 99, ('Fagaras', 'Bucarest') : 211,
            ('Pitesi', 'Rimnicu') : 97, ('Pitesi', 'Craiova') : 138, ('Pitesi', 'Bucarest') : 101,
            ('Bucarest', 'Fagaras') : 211, ('Bucarest', 'Pitesi') : 101
        }
 
        if argv[0] not in Romania.edges.keys():
            print ("Ciudad no existe")
            return
 
        # Building aStar path of parents
        parents = aStar(Romania, startCity, endCity)
 
        # Printing the path
        print (pathfromOrigin(startCity, endCity, parents))
         
 
 
if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
