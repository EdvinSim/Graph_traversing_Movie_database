from queue import PriorityQueue
from Movie import Movie
from Actor import Actor

"""
A graph where nodes are Actors and edges are betweeen two actors staring
in the same movie. An edge weight is 10 minus the film's rating. Both
Actors and Movies are classes and both are used as nodes while traversing 
the graph beacause this makes it easyer. But when counting number of nodes
it only counts Actors.
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

        print(f"\nNodes: {len(self.actors)}\nEdges: {int(edges)}")


    #Oppgave 2
    #Breadth First Search.
    #Finds the shortest path from one actor to another in a unweighted graph.
    def shortestPath(self, startId, goalId):
        startActor = self.nodes[startId]
        goalActor = self.nodes[goalId]

        queue = [startActor]

        #A dict where the key is a visited node and value is previous node in path.
        visited = {}
        
        #Start search.
        while len(queue) > 0:

            pointer = queue.pop(0)

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


    #Prints a path.
    def printPath(self, path: list):

        print("\n" + path[0].name)

        for i in range(1, len(path), 2):
            print(f"===[ {path[i].title} ({path[i].rating}) ] ===> {path[i+1].name}")


    #Prints total weight of a path. Not in use anymore.
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
    #Uses Dijekstra to give the path with the best movie rating from startActor to a goalActor
    def chillestPath(self, startId, goalId):

        startActor = self.nodes[startId]
        goalActor = self.nodes[goalId]

        visited = set()
        dist = {} #Length from node/key to startActor.
        paths = {startActor: None} #Previous node with shortest path to startActor.
        queue = PriorityQueue()
        queue.put((0, startActor))

        infinite = float("inf") #Equivilant to infinite

        #Make default distance from node to start infinite for all nodes.
        for key in self.nodes:
            dist[self.nodes[key]] = infinite
            
        dist[startActor] = 0

        #Find distances from nodes to start
        while not queue.empty():

            node = queue.get()[1]

            if node not in visited:
                visited.add(node)

                for neighbour in node.getNeighbours():
                    currentDist = dist[node] + self.edgeWeight(node, neighbour)
                    if currentDist < dist[neighbour]:
                        dist[neighbour] = currentDist
                        queue.put((currentDist, neighbour)) #Add neighbour with priority currentDist.

                        #Update best path to current node
                        paths[neighbour] = node
            
            #We could not break here and go trough the whole graph, but its takes a while...
            if node == goalActor:
                break
        
        #Make path from start to goal.
        finalPath = []
        tmp = goalActor
        while tmp != None:
            finalPath.insert(0, tmp)
            tmp = paths[tmp]

        return (finalPath, dist[goalActor]/2) #The weight is doubble because we count movies as nodes.


    #Oppgave 4
    #Goes trought the graph, finds all components and writes out the size.
    #Only Actors are counted as nodes.
    def analyzeComponents(self):

        componentSizes = {} #For storing component sizes
        unvisitedActors = set(self.actors.values()) #Used for counting each component size.

        while len(unvisitedActors) > 0:
            before = len(unvisitedActors)

            actor = unvisitedActors.pop()
            self.findComponent(actor, unvisitedActors)

            after = len(unvisitedActors)
            compSize = before - after

            if compSize in componentSizes:
                componentSizes[compSize] += 1
            else:
                componentSizes[compSize] = 1

        #Print component sizes descending on key.
        sortedKeys = list(componentSizes.keys())
        sortedKeys.sort(reverse=True)

        for key in sortedKeys:
            print(f"There are {componentSizes[key]} \tcomponents of size {key}")


    #Visits all nodes from a start node in a component.
    def findComponent(self, startNode, unvisitedActors: set):
        visited = set()
        visited.add(startNode)

        queue = set() #This is not a true queue.
        queue.add(startNode)

        #Visit all nodes in component.
        while len(queue) > 0:
            node = queue.pop()

            for neighbour in node.getNeighbours():
                if neighbour not in visited:
                    queue.add(neighbour)
                    visited.add(neighbour)

                    if isinstance(neighbour, Actor):
                        unvisitedActors.remove(neighbour)







    #Only wokrs on test.py. DFS on imdb graph will reach max recursion quicky.
    def DFS_Recursive(self, node, visited: set, unvisitedActors: set):
        visited.add(node)

        for neighbour in node.getNeighbours():
            if neighbour not in visited:
                if isinstance(neighbour, Actor):
                    unvisitedActors.remove(neighbour)
                self.DFS_Recursive(neighbour, visited, unvisitedActors)


    #Only wokrs on test.py. Takes too long on imdb graph.
    def DFS_Iterative(self, startNode: Actor, unvisitedActors: set):
        visited = set()
        stack = [startNode]

        while len(stack) > 0:
            node = stack.pop(0)

            if node not in visited:
                visited.add(node)

                if isinstance(node, Actor) and node != startNode:
                    unvisitedActors.remove(node)

                for neighbour in node.getNeighbours():
                    stack.insert(0, neighbour)


