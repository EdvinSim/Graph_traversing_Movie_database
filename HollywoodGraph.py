from queue import PriorityQueue
from Movie import Movie
from Actor import Actor
import sys

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

        for key in self.movies:
            edges += len(self.movies[key].actors)

        print(f"\nNodes: {len(self.nodes)}\nEdges: {edges}")


    #Oppgave 2
    #Bredde-foerst soek
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


    def printPath(self, path: list):

        print("\n" + path[0].name)

        for i in range(1, len(path), 2):
            print(f"===[ {path[i].title} ({path[i].rating}) ] ===> {path[i+1].name}")

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

        visited = []
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
                visited.append(u)

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
    #DFS full
    def analyzeComponents(self):

        componentSizes = {}
        visited = []

        for node in list(self.nodes.values()):
            if node not in visited:
                print("New component") #TODO fjern
                before = len(visited)
                self.DFS_Iterative(node, visited)
                after = len(visited)
                compSize = after - before

                if compSize in componentSizes:
                    componentSizes[compSize] += 1
                else:
                    componentSizes[compSize] = 1

        for key in componentSizes:
            print(f"There are {componentSizes[key]} components of size {key}")


    #Uses DFS to define a component. visited = component.
    def DFS_Recursive(self, node, visited: list):
        visited.append(node)

        for neighbour in node.getNeighbours():
            if neighbour not in visited:
                self.DFS_Recursive(neighbour, visited)




    #Uses DFS to return a component
    def DFS_Iterative(self, startNode, visited: list):
        print("Iterative")#TODO fjern
        stack = [startNode]

        while len(stack) > 0:
            node = stack.pop(0)

            if node not in visited:
                visited.append(node)

                for neighbour in node.getNeighbours():
                    stack.insert(0, neighbour)