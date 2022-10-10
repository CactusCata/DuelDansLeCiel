import cProfile
import pstats

def startGame(runMethod):

    with cProfile.Profile() as pr:
        runMethod()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename='profiling.prof')
