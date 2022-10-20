class Actor:

    #A node class for a graph of movies and actors.
    #For simplicity there are no get methods and all class variables are public.

    def __init__ (self, nmId: str, name: str):
        self.nmId = nmId
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

    def __str__(self) -> str:
        string = "\n"
        string += self.name + ":"

        for movie in self.movies:
            string += "\n\t" + movie.title

        return string
