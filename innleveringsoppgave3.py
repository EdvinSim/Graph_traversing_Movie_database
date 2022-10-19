#IN2010, innelvering 3

from Movie import Movie
from Actor import Actor

#Oppgave 1.1
#Create graph.
movies = Movie.readFile("marvel_movies.tsv")
actors = Actor.readFile("marvel_actors.tsv", movies)

nodes = {}
edges = []

for key in movies:
    edges += movies[key].getEdges()

nodes.update(movies)
nodes.update(actors)


#Oppgave 1.2
def graphSize(nodes: dict, edges: list):
    print(f"\nOppgave 1\n\nNodes: {len(nodes)}\nEdges: {len(edges)}")

graphSize(nodes, edges)


#Oppgave 2
#Bredde-foerst soek
#TODO ikke ferdig. Burde ta inn ID ikke objekt.
#TODO Lage egen printPath metode?
def shortestPath(startActor, goalActor):
    queue = [startActor]
    visited = []
    paths = {}

    while len(queue) > 0:

        pointer = queue[0]

        for node in pointer.neighbours:
            if node not in visited:
                if node == goalActor:
                    shortestPath = [pointer, node]
                    tmp = pointer
                    
                    while tmp != startActor:
                        shortestPath.insert(0, paths[tmp])
                        tmp = paths[tmp]

                    return shortestPath

                else:
                    visited.append(node)
                    queue.append(node)
                    paths[node] = queue[0]
        queue.pop(0)