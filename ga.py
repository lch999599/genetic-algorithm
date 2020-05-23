import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
import random
from itertools import combinations
from selection import TournamentSelection
from config import Config

random.seed(99)

def generate_chromosomes():
    chrs = []
    for i in range(Config.POPULATION_SIZE):
        chrs.append(random.sample(range(1, 30), Config.VARIABLES))
    return chrs

def calculate_fitnesses(chromosomes):
    fitness = []
    fitness_dict = dict()
    for idx, i in enumerate(chromosomes):
        obj = Config.OBJ_FUN(*i)
        if obj == 0:
            # print(f"Objective Achieved: {i}")
            return i, True
        fitness_score = 1 / (obj)
        fitness_dict[idx+1] = fitness_score
    return fitness_dict, False

def crossover(chromosomes, crossover_rate=0.25):
    R = [random.uniform(0, 1) for i in range(Config.POPULATION_SIZE)]
    fitness = []
    for i in chromosomes:
        obj = Config.OBJ_FUN(*i)
        _fitness = 1/(obj+1)
        fitness.append(_fitness)
    new_parent_index = []
    for idx, val in enumerate(R):
        if val < crossover_rate:
            new_parent_index.append(idx)
    crossover_list = list(combinations(new_parent_index, 2))
    done_list = []
    for i in crossover_list:
        if i[0] not in done_list:
            _to = i[0]
            _from = i[1]
        else:
            _to = i[1]
            _from = i[0]
        crossover_point = random.randint(1, Config.VARIABLES+1)
        child = list(chromosomes[_to][:crossover_point]) + list(chromosomes[_from][crossover_point:])
        chromosomes[_to] = child
    return chromosomes

def mutation(chromosomes, mutation_rate=0.25):
    number_of_mutations = int(Config.VARIABLES*Config.POPULATION_SIZE*mutation_rate)
    mutations_points = [random.randint(1, Config.VARIABLES*Config.POPULATION_SIZE-1) for i in range(number_of_mutations)]
    mutations_values = [random.randint(1, 30) for i in range(number_of_mutations)]
    for i in range(number_of_mutations):
        row = mutations_points[i] // Config.VARIABLES
        col = (mutations_points[i] % Config.VARIABLES)-1
        chromosomes[row][col] = mutations_values[i]
    return chromosomes

def run():
    chromosomes = generate_chromosomes()
    print(f"Initial Population    : {chromosomes}")

    fitness_history = []
    obj_fn_history = []

    for i in tqdm(range(Config.ITERATIONS)):
        fitness, complete = calculate_fitnesses(chromosomes)
        # print(f"Fitness               : {fitness}")
        if complete:
            obj_fn_history.append(0)
            fitness_history.append(1)
            solution = fitness
            break
        fitness_history.append(max(fitness.values()))
        obj_fn_history.append(min(Config.OBJ_FUN(*i) for i in chromosomes))
        
        selection = TournamentSelection(chromosomes, fitness)
        # print(f"Tournament Selection  : {selection}")
        
        cross = crossover(selection, crossover_rate=0.7)
        # print(f"Crossover             : {cross}")

        chromosomes = mutation(cross, mutation_rate=0.1)
        # print(f"Mutated Chromosomes   : {chromosomes}")
    plt.figure(figsize=(10, 12))
    plt.suptitle(f"Total Generations: {i}\nFitness Value: {fitness_history[-1]}\nObjective Function Value: {obj_fn_history[-1]}\nSolution: {solution}")
    plt.subplot(1, 2, 1)
    plt.title('Fitness values')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.plot(range(1, len(fitness_history)+1), fitness_history, color='blue')
    
    plt.subplot(1, 2, 2)
    plt.title('Objective values')
    plt.xlabel('Generations')
    plt.ylabel('Objective Value')
    plt.plot(range(1, len(obj_fn_history)+1), obj_fn_history, color='green')
    plt.show()

if __name__ == '__main__':
    run()