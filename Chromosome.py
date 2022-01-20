from random import randint


def generateARandomPermutation(n, lista):
    perm = [i for i in range(1, n) if i not in lista]
    pos1 = randint(0, len(perm) - 1)
    pos2 = randint(0, len(perm) - 1)
    if len(perm) <= 2:
        return perm
    while pos2 == pos1:
        pos2 = randint(0, len(perm) - 1)
    if pos2 < pos1:
        pos1, pos2 = pos2, pos1
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


class Chromosome:

    def __init__(self, source_city, det_city, prblParam=None, no=None):
        # prblParam aici e number_of_cities
        self.__prblParam = prblParam
        self.__source_city = source_city
        self.__dest_city = det_city
        if prblParam is not None and no is None:
            pair = [self.__source_city, self.__dest_city]
            self.__repres = generateARandomPermutation(self.__prblParam['noNodes'], pair)
            self.repres_init()
        self.__fitness = 0.0

    def repres_init(self):
        self.__repres.insert(0, self.__source_city)
        self.__repres.append(self.__dest_city)
        # self.__repres[0] = self.__source_city
        # self.__repres[self.__prblParam['noNodes'] - 1] = self.__dest_city

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=None):
        self.__repres = l

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

    def calculate_fitness(self, distance_each_city):
        sum = 0
        for i in range(0, self.__prblParam['noNodes'] - 1):
            sum += distance_each_city[self.__repres[i] - 1][self.__repres[i + 1] - 1]
        sum += distance_each_city[self.__source_city - 1][self.__dest_city - 1]
        self.__fitness = sum

    def prblParam(self):
        return self.__prblParam

    def crossover(self, c):
        # order XO
        start = c.__repres[0]
        del c.__repres[0]
        del self.__repres[0]
        dest = self.__repres[self.__prblParam['noNodes'] - 2]
        del self.__repres[self.__prblParam['noNodes'] - 2]
        del c.__repres[self.__prblParam['noNodes'] - 2]

        pos1 = randint(-1, self.__prblParam['noNodes'] - 2)
        pos2 = randint(-1, self.__prblParam['noNodes'] - 2)
        if pos2 < pos1:
            pos2, pos1 = pos1, pos2
        k = 0
        newrepres = self.__repres[pos1:pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < (self.__prblParam['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        newrepres.insert(0, start)
        newrepres.append(dest)
        c.__repres.insert(0, start)
        c.__repres.append(dest)
        self.__repres.insert(0, start)
        self.__repres.append(dest)
        offspring = Chromosome(self.__source_city, self.__dest_city, self.__prblParam, no=1)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # mutates the chromosome
        nr=randint(1,(self.__prblParam['noNodes'] - 2)/2)
        for index in range(nr):
            pos1 = randint(1, self.__prblParam['noNodes'] - 2)
            pos2 = randint(1, self.__prblParam['noNodes'] - 2)
            if pos2 < pos1:
                pos1, pos2 = pos2, pos1
            if pos2 == pos1:
                if pos2 != 1:
                    pos1 -= 1
                else:
                    pos2 += 1
            el = self.__repres[pos2]
            del self.__repres[pos2]
            self.__repres.insert(pos1 + 1, el)

    def source_city(self):
        return self.__source_city

    def destination_city(self):
        return self.__dest_city

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fitness: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
