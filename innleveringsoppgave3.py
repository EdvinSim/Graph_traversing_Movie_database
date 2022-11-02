from tracemalloc import start
from HollywoodGraph import HollywoodGraph
import time

#IN2010, innelvering 3

def main():
    startTime = time.time()

    imdb = HollywoodGraph("movies.tsv", "actors.tsv")
    
    # print("\nOppgave 1")
    # imdb.printGraphSize()

    # #Tuples of actor pairs. index 0 = start. index 1 = goal.
    # actorPairs = [("nm2255973", "nm0000460"), ("nm0424060", "nm0000243"), ("nm4689420", "nm0000365"), ("nm0000288", "nm0001401"), ("nm0031483", "nm0931324")]
    
    # print("\nOppgave 2")
    # for pair in actorPairs:
    #     imdb.printPath(imdb.shortestPath(pair[0], pair[1]))

    # print("\nOppgave 3")
    # for pair in actorPairs:
    #     path = imdb.chillestPath(pair[0], pair[1])
    #     imdb.printPath(path)
    #     imdb.printTotalWeight(path)

    print("\nOppgave 4\n")
    imdb.analyzeComponents()

    print("\nTime used for all tasks:", time.time() - startTime, "sec.")

main()