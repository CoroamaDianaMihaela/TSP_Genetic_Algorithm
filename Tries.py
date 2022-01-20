##"--------------------------------"B

#
# last_chrm.append(Chromosome(parent1.source_city(), parent1.destination_city(), parent1.prblParam()))
# last_chrm.append(Chromosome(parent1.source_city(), parent1.destination_city(), parent1.prblParam()))
# last_chrm.append(Chromosome(parent1.source_city(), parent1.destination_city(), parent1.prblParam()))

##"--------------------------------"3

# for x in last_chrm:
#     ok = 0
#     for val in best_chrms:
#         if x.repres == val.repres:
#             ok = 1
#     if ok == 0:
#         x.calculate_fitness(distance_per_city)
#         interm_chromosome = x
#         best_chrms.append(interm_chromosome)
#         x.mutation()
#         best_chrms.append(x)

##"--------------------------------"2

# for x in last_chrm:
#     ok = 0
#     for val in best_chrms:
#         if x.repres == val.repres:
#             ok = 1
#     if ok == 0:
#         x.calculate_fitness(distance_per_city)
#         if x != best_chrms[0]:
#             x.mutation()
#             best_chrms.append(x)
#         else:
#             best_chrms.append(x)

##"--------------------------------"1