from Actor import Actor
from Movie import Movie

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

#smallTest()
testMarvel()