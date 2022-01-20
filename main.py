from datetime import time

from Utils import load_data_TXT, GA, load_data_TSP
from tqdm import tqdm
import time

"""
This is GA algorithm that determines the shortest path between two given nodes , the path will contain all the
 possible nodes
"""

def run():
    # name = "hardE.txt"
    name = "hard_tsp_ch.txt"
    if name != "hardE.txt":
        prblParam, distance_per_city, source_city, dest_city = load_data_TXT(name)
    else:
        prblParam, distance_per_city, source_city, dest_city = load_data_TSP(name)
    # Chrms=int(input('How many chromosomes do you want to be at the same time? :'))
    # I wanted to see the total average of the best distance determined by the algorithm
    average_total = 0
    average = 0
    for _ in tqdm(range(100)):
        average += GA(prblParam, distance_per_city, source_city, dest_city, 10)
        time.sleep(0.5)

    average_total = average / 100
    print(average_total)

run()
