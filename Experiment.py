from Chromosome import Chromosome


def testXO():
    # seeing what the crossover does to a chromosome
    prblParam = {'noNodes': 10}
    c1 = Chromosome(prblParam)
    c2 = Chromosome(prblParam)
    off = c1.crossover(c2)
    print("parent : ", c1)
    print("parent : ", c2)
    print(off)


def testMutation():
    prblParam = {'noNodes': 10}
    c1 = Chromosome(prblParam)
    print("before", c1)
    c1.mutation()
    print("after", c1)


testXO()
testMutation()
