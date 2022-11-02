from queue import PriorityQueue
from Movie import Movie
from Actor import Actor

"""
A graph where nodes are Actors and edges are betweeen two actors staring
in the same movie. The edge weight is 10 minus the films rating. Both
Actors and Movies are classes and both are used as nodes while traversing 
the graph beacause this makes it easyer. But when counting number of nodes
it only count Actors.
"""

class HollywoodGraph:

    #Oppgave 1.1
    def __init__(self, moviesFileName, actorsFileName):
        self.movies = Movie.readFile(moviesFileName)
        self.actors = Actor.readFile(actorsFileName, self.movies)
        self.nodes = {}

        self.nodes.update(self.movies)
        self.nodes.update(self.actors)


    #Oppgave 1.2
    def printGraphSize(self):
        edges = 0

        for film in list(self.movies.values()):
            numActors = len(film.actors)
            edges += (numActors*(numActors - 1))/2

        print(f"\nNodes: {len(self.actors)}\nEdges: {edges}")


    #Oppgave 2
    #Breadth first search.
    #Finds the shortest path from one actor to another in a unweighted graph.
    def shortestPath(self, startId, goalId):
        startActor = self.nodes[startId]
        goalActor = self.nodes[goalId]

        queue = [startActor]

        #A dict where the key is a visited node and value is previous node in path.
        visited = {}

        while len(queue) > 0:

            pointer = queue[0]

            for node in pointer.getNeighbours():
                if node not in visited:
                    visited[node] = pointer
                    
                    #Create path.
                    if node == goalActor:
                        shortestPath = [node]
                        tmp = node
                        
                        while tmp != startActor:
                            shortestPath.insert(0, visited[tmp])
                            tmp = visited[tmp]

                        return shortestPath

                    else:
                        queue.append(node)

            queue.pop(0)

    #Prints a path.
    def printPath(self, path: list):

        print("\n" + path[0].name)

        for i in range(1, len(path), 2):
            print(f"===[ {path[i].title} ({path[i].rating}) ] ===> {path[i+1].name}")


    #Prints total weight of a path.
    def printTotalWeight(self, path: list):
        total = 0
        for i in range(1, len(path), 2):
            total += self.edgeWeight(path[i], path[i+1])
        print(f"Total weight: {total}" )

    
    #Returns the weight of an edge
    def edgeWeight(self, node1, node2):
        if isinstance(node1, Movie):
            movie = node1
        else:
            movie = node2
        return 10 - movie.rating


    #Oppgave 3
    #Uses Dijekstra to give the path with the best movie rating from a startActor to a goalActor
    def chillestPath(self, startId, goalId):

        startActor = self.nodes[startId]
        goalActor = self.nodes[goalId]

        visited = set()
        dist = {} #Length from node(key) to startActor.
        paths = {startActor: None} #Previous node with shortest path to startActor.
        queue = PriorityQueue()
        queue.put((0, startActor))

        infinite = float("inf") #Equivilant to infinite

        #Make default distance from node to start infinite for all nodes.
        for key in self.nodes:
            dist[self.nodes[key]] = infinite
            
        dist[startActor] = 0

        #Find distances from nodes to start
        while not queue.empty() > 0 and len(visited) < len(self.nodes):

            u = queue.get()[1]

            if u not in visited:
                visited.add(u)

                for v in u.getNeighbours():
                    c = dist[u] + self.edgeWeight(u, v)
                    if c < dist[v]:
                        dist[v] = c
                        queue.put((c, v)) #Legg til v med prioritet c.

                        #Update best path to current node
                        paths[v] = u
            
            #We could not break here and go trough the whole graph, but its takes a while...
            if u == goalActor:
                break
        
        #Make path from start to goal.
        finalPath = []
        tmp = goalActor
        while tmp != None:
            finalPath.insert(0, tmp)
            tmp = paths[tmp]

        return finalPath


    #Oppgave 4
    #Goes trought tha graph, finds all components and writes out the size.
    #Only Actors are counted as nodes. Therefore there are two different sets of visited.
    def analyzeComponents(self):

        componentSizes = {}
        visitedAll = set()
        visitedActors = set()

        for actor in list(self.actors.values()):
            if actor not in visitedAll:
                before = len(visitedActors)
                self.BFS(actor, visitedAll, visitedActors)
                after = len(visitedActors)
                compSize = after - before

                if compSize in componentSizes:
                    componentSizes[compSize] += 1
                else:
                    componentSizes[compSize] = 1

        #Print component sizes descending on key.
        sortedKeys = list(componentSizes.keys())
        sortedKeys.sort(reverse=True)

        for key in sortedKeys:
            print(f"There are {componentSizes[key]} \tcomponents of size {key}")


    #Not working. TODO fjern?
    def DFS_Recursive(self, node, visited: set):
        visited.add(node)

        for neighbour in node.getNeighbours():
            if neighbour not in visited:
                self.DFS_Recursive(neighbour, visited)


    #Not working. TODO fjern?
    def DFS_Iterative(self, startNode: Actor, visited: set):
        stack = [startNode]

        while len(stack) > 0:
            node = stack.pop(0)

            #TODO fjern
            length = len(visited)
            if length % 1000 == 0:
                print(length)

            if node not in visited:
                visited.add(node)

                for neighbour in node.getNeighbours():
                    stack.insert(0, neighbour)


    #Breadt First Search to find all nodes in a component.
    def BFS(self, startNode, visitedAll: set, visitedActors: set):
        queue = [startNode]

        #Add startNode so that there will be no components of size zero.
        if isinstance(startNode, Actor):
            visitedActors.add(startNode)

        #Visit all nodes in component.
        while len(queue) > 0:
            node = queue.pop(0)

            for neighbour in node.getNeighbours():
                if neighbour not in visitedAll:
                    queue.append(neighbour)
                    visitedAll.add(neighbour)

                    if isinstance(neighbour, Actor):
                        visitedActors.add(neighbour)