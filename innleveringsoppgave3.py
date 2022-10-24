#IN2010, innelvering 3

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


#Oppgave 3
#Gives the path with the best movie rating from a startActor to a goalActor
def chillestPath(startActor, goalActor):
    visited = []
    dist = {}#TODO default uendelig
    priQueue = []
    dist[startActor] = 0

    while len(priQueue) > 0:
        #Pointer = u fra foiler TODO fjern.
        pointer = priQueue.pop(0)
        if pointer not in visited:
            visited.append[pointer]

            for edge in pointer.getEdges():
                tmp = dist.setdefault(pointer , float["inf"]) #If key not in dist set value as infinite.
                distanceToEdge = tmp + edge.weight

                if distanceToEdge < dist.setdefault(edge.actor2, float("inf")):
                    dist[edge.actor2] = distanceToEdge
                    priQueue.append(distanceToEdge, edge.actor2)

    return dist
                    


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



main()