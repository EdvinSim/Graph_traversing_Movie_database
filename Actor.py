import Movie

class Actor:

    #A node class for a graph of movies and actors.
    #For simplicity there are no get methods and all class variables are public.

    def __init__ (self, nmId: str, name: str):
        self.id = nmId
        self.name = name
        self.movies = []

    #returns a dictionary of actors with nmId as key.
    def readFile(filename: str, movies: list):
        actors = {}
        file = open(filename, "r", encoding = "utf-8")

        for line in file:
            line = line.strip().split("\t")
            newActor = Actor(line[0], line[1])
            actors[line[0]] = newActor

            #Movies from file that is not in the dict movies are ignored
            for ttId in line[2:]:
                if ttId in movies:
                    movie = movies[ttId]
                    newActor.movies.append(movie)
                    movie.actors.append(newActor)

        file.close()

        return actors


    def getNeighbours(self):
        return self.movies

    #Returns all MovieEdges from actor. TODO fjern hvis ikke blir brukt.
    def getMovieEdges(self):
        edges = []
        for movie in self.movies:
            for actor in movie.actors:
                edges.append(MovieEdge(actor, movie))
        
        return edges


    def __str__(self) -> str:
        string = "\n"
        string += self.name + ":"

        for movie in self.movies:
            string += "\n\t" + movie.title

        return string

    def __gt__(self, other):
        if isinstance(other, Movie.Movie):
            return self.name > other.title
        else:
            return self.name > other.name

    def __lt__(self, other):
        if isinstance(other, Movie.Movie):
            return self.name < other.title
        else:
            return self.name < other.name

#An edge representing a movie between two actors. #TODO fjern hvis denne klasssen ikke ble brukt.
class MovieEdge:
    def __init__(self, actor, movie):
        self.actor1 = self
        self.actor2 = actor
        self.weight = "%0.1f" % (10 - movie.rating)