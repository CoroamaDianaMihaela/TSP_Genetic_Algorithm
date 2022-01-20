from Chromosome import Chromosome
import math


def load_data_TXT(fileName):
    """

    :param fileName: the name of the file from which we take the information
    :return: None
    """
    f = open(fileName, "r")
    number_cities = int(f.readline())
    print(number_cities)
    distance_per_city = [[0] for _ in range(0, number_cities)]
    for _ in range(0, number_cities):
        numbers = f.readline()
        numbers = numbers.split(',')
        distance_per_city[_] = []
        for number in numbers:
            distance_per_city[_].append(int(number))

    source_city = f.readline()
    if source_city != '':
        source_city = int(source_city)
    else:
        source_city = number_cities
    dest_city = f.readline()
    if dest_city != '':
        dest_city = int(dest_city)
    else:
        dest_city = 1
    f.close()
    prblParam = {'noNodes': number_cities}
    return prblParam, distance_per_city, source_city, dest_city


def calculate_distances(coordinates, number_cities):
    """
    Calculates the distance between each node and make a matrix named distance_each_city in which we store it
    :param coordinates: list, which has the coordinates of each node
    :param number_cities: int , how many cities there are
    :return: a matrix that contains the distanced between the nodes
    """
    distance_each_city = [[] for _ in range(0, number_cities)]
    for v in range(0, len(coordinates)):
        for v_2 in range(0, len(coordinates)):
            if v != v_2:
                x = (coordinates[v][0] - coordinates[v_2][0]) ** 2
                y = (coordinates[v][1] - coordinates[v_2][1]) ** 2
                distance_each_city[v].append(int(math.sqrt(x + y)))
            else:
                distance_each_city[v].append(0)

    return distance_each_city


def load_data_TSP(fileName):
    """
      :param fileName: the name of the file from which we take the information
      :return: None
      """
    f = open(fileName, 'r')
    for _ in range(0, 6):
        buffer = f.readline()
    coordinates = []
    nr_c = 0
    ok = 1
    while ok:
        coordinate = f.readline()
        if coordinate == "EOF":
            nr_c = int(len(coordinates))
            break
        else:
            coordinate = coordinate.split()
        coordinates.append((int(coordinate[1]), int(coordinate[2])))

    number_cities = nr_c
    source_city = number_cities
    dest_city = 1
    distance_per_city = calculate_distances(coordinates, number_cities)
    f.close()
    prblParam = {'noNodes': number_cities}
    return prblParam, distance_per_city, source_city, dest_city


def best_three_chromosomes(chromosomes):
    """
    Determines the best three chromosomes and make a list which contains the best three chromosomes
     their offspring and a mutation of each offspring
    :param chromosomes: list of random chromosomes
    :return: chrms: a list made of 9 chromosomes
    """
    best_chrms = sorted(chromosomes, key=lambda x: x.fitness, reverse=False)
    chrms = [best_chrms[i] for i in range(0, 3)]
    crossover_the_best(chrms)
    return chrms


def crossover_the_best(best_chrms):
    """
    The function adds to best_chrms the offsprings from the three offsprings and for each a mutation
    :param best_chrms: a list of three chromsomes which has the best fitness
    :return:None
    """
    parent1 = best_chrms[0]
    parent2 = best_chrms[1]
    parent3 = best_chrms[2]

    last_chrm = [parent1, parent2, parent3]

    offspring_1 = parent1
    offspring_1.mutation()
    offspring_2 = parent2
    offspring_2.mutation()
    offspring_3 = parent3
    offspring_3.mutation()

    offspring_4 = parent1.crossover(parent2)
    offspring_5 = parent1.crossover(parent3)
    offspring_6 = parent1.crossover(offspring_2)
    offspring_7 = parent1.crossover(offspring_3)
    offspring_8 = parent2.crossover(offspring_1)
    offspring_9 = parent3.crossover(offspring_1)

    last_chrm.append(offspring_1)
    last_chrm.append(offspring_2)
    last_chrm.append(offspring_3)
    last_chrm.append(offspring_4)
    last_chrm.append(offspring_5)
    last_chrm.append(offspring_6)
    last_chrm.append(offspring_7)
    last_chrm.append(offspring_8)
    last_chrm.append(offspring_9)

    for x in last_chrm:
        ok = 0
        for val in best_chrms:
            if x.repres == val.repres:
                ok = 1
        if ok == 0:
            best_chrms.append(x)


def best_chromosome(chrms):
    """

    :param chrms: a list of chromosomes
    :return: the best chromosome
    """
    lista = sorted(chrms, key=lambda x: x.fitness, reverse=False)
    return lista[0]


def GA(prblParam, distance_per_city, source_city, dest_city, gens):
    """
    :param prblParam: dictionary, which contains the number of cities
    :param distance_per_city: matrix
    :param source_city: int
    :param dest_city: int
    :param gens: int,how many generations
    :return:
    """

    chromosomes = []
    best_chrms = Chromosome(source_city, dest_city)
    for _ in range(0, 9):
        c1 = Chromosome(source_city, dest_city, prblParam)
        c1.calculate_fitness(distance_per_city)
        chromosomes.append(c1)
    intermediate_chromosomes = chromosomes
    for _ in range(0, gens):
        GA_chromosomes = best_three_chromosomes(intermediate_chromosomes)
        for x in GA_chromosomes:
            if x.fitness == 0:
                x.calculate_fitness(distance_per_city)
        best_chrms = best_chromosome(GA_chromosomes)
        intermediate_chromosomes = []
        for x in GA_chromosomes:
            if x not in intermediate_chromosomes:
                intermediate_chromosomes.append(x)
        if len(intermediate_chromosomes) <= 2:
            break

    return best_chrms.fitness
