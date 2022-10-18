class Movie:

    #A edge class for a graph of movies and actors.
    #For simplicity there are no get methods and all class variables are public.

    def __init__(self, ttId: str, title: str, rating: float, votes: int):
        self.ttId = ttId
        self.title = title
        self.rating = rating
        self.votes = votes
        self.actor1 = None
        self.actor2 = None

    #Returns a dictonary of movie objects with ttId as keys.
    def readFile(filename: str):
        movies = {}
        file = open(filename)

        for line in file:
            line = line.strip().split("\t")
            movies[line[0]] = Movie(line[0], line[1], line[2], line[3])

        file.close()

        return movies

    def __str__(self) -> str:
        return f"\n{self.title}:\n\tID: {self.ttId}\n\trating: {self.rating}\n\tvotes: {self.votes}"