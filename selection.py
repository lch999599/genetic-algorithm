from config import Config
import random

def TournamentSelection(chromosomes, fitness):
    number_of_tournaments = Config.POPULATION_SIZE
    new_population = []
    for i in range(number_of_tournaments):
        select = False
        while not select:
            pop1 = random.choice(range(1, Config.POPULATION_SIZE+1))
            pop2 = random.choice(range(1, Config.POPULATION_SIZE+1))
            if pop1 != pop2:
                select = True
        if fitness[pop1] >= fitness[pop2]:
            new_population.append(pop1)
        else:
            new_population.append(pop2)
    new_pop = []
    for i in new_population:
        new_pop.append(chromosomes[i-1])
    return new_pop