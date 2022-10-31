

#IN2010, innelvering 3

from queue import PriorityQueue
from Movie import Movie
from Actor import Actor

#Oppgave 1.1
#Create graph.
def buildGraph(nodes: dict, edges: list):
    movies = Movie.readFile("movies.tsv")
    actors = Actor.readFile("actors.tsv", movies)

    for key in movies:
        edges += movies[key].getEdges()

    nodes.update(movies)
    nodes.update(actors)


#Oppgave 1.2
def graphSize(nodes: dict, edges: list):
    print(f"\nOppgave 1\n\nNodes: {len(nodes)}\nEdges: {len(edges)}")


#Oppgave 2
#Bredde-foerst soek
def shortestPath(startActor, goalActor):

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


def printPath(path: list):

    print("\n" + path[0].name)

    for i in range(1, len(path), 2):
        print(f"===[ {path[i].title} {path[i].rating} ] ===> {path[i+1].name}")

#Edge
def edgeWeight(node1, node2):
    if isinstance(node1, Movie):
        movie = node1
    else:
        movie = node2
    return float("%0.1f" % (10 - movie.rating))

#Oppgave 3
#Dijkstra
#Gives the path with the best movie rating from a startActor to a goalActor
#TODO legge til total vekt i print ogsaa;
def chillestPath(nodes, startActor, goalActor):
    visited = []
    dist = {} #Length from node(key) to startActor.
    paths = {startActor: None} #Previous node with shortest path to startActor.
    queue = PriorityQueue()
    queue.put((0, startActor)) #Priority queue

    infinite = float("inf") #Equivilant to infinite

    #Make default distance from node to start infinite for all nodes.
    for key in nodes:
        dist[nodes[key]] = infinite
    dist[startActor] = 0

    #Find distances from nodes to start
    while not queue.empty() > 0 and len(visited) < len(nodes):

        u = queue.get()[1]

        if u not in visited:
            visited.append(u)

            for v in u.getNeighbours():
                c = dist[u] + edgeWeight(u, v)
                if c < dist[v]:
                    dist[v] = c
                    queue.put((c, v)) #Legg til v med prioritet c.

                    #Update best path to current node
                    paths[v] = u
        
        if u == goalActor:
            break
    
    #Make path from start to goal.
    finalPath = []
    tmp = goalActor
    while tmp != None:
        finalPath.insert(0, tmp)
        tmp = paths[tmp]

    return finalPath
                    


def main():

    nodes = {}
    edges = []
    buildGraph(nodes, edges)
    graphSize(nodes, edges)

    #Her blir det riktig antall steg, men andre filmer enn fasiten i oppgaven
    #siden en node sine naboer er i forskjellig rekkefolge.
    
    print("\nOppgave 2")
    printPath(shortestPath(nodes["nm2255973"], nodes["nm0000460"]))
    printPath(shortestPath(nodes["nm0424060"], nodes["nm0000243"]))
    printPath(shortestPath(nodes["nm4689420"], nodes["nm0000365"]))
    printPath(shortestPath(nodes["nm0000288"], nodes["nm0001401"]))
    printPath(shortestPath(nodes["nm0031483"], nodes["nm0931324"]))

    print("\nOppgave 3")
    # printPath(chillestPath(nodes, nodes["nm2255973"], nodes["nm0000460"]))
    printPath(chillestPath(nodes, nodes["nm2255973"], nodes["nm0000460"]))
    printPath(chillestPath(nodes, nodes["nm2255973"], nodes["nm0000460"]))
    printPath(chillestPath(nodes, nodes["nm0424060"], nodes["nm0000243"]))
    printPath(chillestPath(nodes, nodes["nm4689420"], nodes["nm0000365"]))
    printPath(chillestPath(nodes, nodes["nm0000288"], nodes["nm0001401"]))
    printPath(chillestPath(nodes, nodes["nm0031483"], nodes["nm0931324"]))

main()