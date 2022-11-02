import Actor

class Movie:

    #A edge class for a graph of movies and actors.
    #For simplicity there are no get methods and all class variables are public.

    def __init__(self, ttId: str, title: str, rating: float, votes: int):
        self.id = ttId
        self.title = title
        self.rating = float(rating)
        self.votes = int(votes)
        self.actors = []

    #Returns a dictonary of movie objects with ttId as keys.
    def readFile(filename: str):
        movies = {}
        file = open(filename, "r", encoding = "utf-8")

        for line in file:
            line = line.strip().split("\t")
            movies[line[0]] = Movie(line[0], line[1], line[2], line[3])

        file.close()

        return movies

    def __str__(self) -> str:
        string =  f"\n{self.title}:\n\tID: {self.ttId}\n\tRating: {self.rating}\n\tVotes: {self.votes}\n\tActors:"
        
        for actor in self.actors:
            string += "\n\t\t" + actor.name

        return string


    def getNeighbours(self):
        return self.actors

    def getName(self):
        return self.title

    #TODO er det kasnkje bedre aa ikke ha en egen edge klasse??
    def getEdges(self):
        edges = []

        for actor in self.actors:
            edges.append(Edge(actor, self))

        return edges

    def __gt__(self, other):
        if isinstance(other, Actor.Actor):
            return self.title > other.name
        else:
            return self.title > other.title
    
    def __lt__(self, other):
        if isinstance(other, Actor.Actor):
            return self.title < other.name
        else:
            return self.title < other.title





#Inner class for a graph edge between a movie and a actor. TODO fjern hvis ikke brukt.
class Edge:
    def __init__(self, actor, movie):
        self.actor = actor
        self.movie = movie
        self.weight = "%0.1f" % (10 - movie.rating) #Slik ellers blir det ikke helt riktig output.

    def __str__(self):
        return f"{self.movie.title} <---- {self.weight} ----> {self.actor.name}"