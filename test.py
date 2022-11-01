from Actor import Actor
from Movie import Movie
from HollywoodGraph import HollywoodGraph

def smallTest():
    sw4 = Movie("tt1", "A new Hope", 9.9, 123456)
    sw5 = Movie("tt2", "Empire strikes back", 10.0, 654321)
    edvin = Actor("nm92", "Edvin Simenstad")
    edvin.movies.extend([sw4, sw5])
    print(edvin, sw4, sw5)

def testMarvel():
    marvelMovies = Movie.readFile("marvel_movies.tsv")
    marvelActors = Actor.readFile("marvel_actors.tsv", marvelMovies)

    # for key in marvelActors:
    #     print(marvelActors[key])
    
    for key in marvelMovies:
        print(marvelMovies[key], "\n")

        for edge in marvelMovies[key].getEdges():
            print(edge)

#Outdated
def testPath():
    nodes = {}
    edges = []

    buildGraph(nodes, edges)
    path = shortestPath(nodes["nm0000354"], nodes["nm0000168"]) #From Matt Damon to Samuel L. Jackson
    printPath(path)

#Outdated
def testChill():
    nodes = {}
    edges = []

    buildGraph(nodes, edges)

    shortest = chillestPath(nodes["nm0000354"], nodes["nm0000168"])
    printPath(shortest)


def testComponents(graph: HollywoodGraph):
    graph.analyzeComponents()

print("\nTest:")
graph = HollywoodGraph("marvel_movies.tsv", "marvel_actors.tsv")
# smallTest()
# testMarvel()
# testPath()
# testChill()
testComponents(graph)