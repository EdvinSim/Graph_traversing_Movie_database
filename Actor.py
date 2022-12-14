import Movie

#A node class for a HollywoodGraph of movies and actors.
#For simplicity there are only a few get methods and all class variables are public.

class Actor:

    def __init__ (self, nmId: str, name: str):
        self.nmId = nmId
        self.name = name
        self.movies = set()

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
                    newActor.movies.add(movie)
                    movie.actors.add(newActor)

        file.close()

        return actors


    def getNeighbours(self):
        return self.movies


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