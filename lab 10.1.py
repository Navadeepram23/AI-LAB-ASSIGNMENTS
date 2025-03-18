import random

num_jobs = 10
num_machines = 5
processing_times = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
population_size = 40
generations = 200
mutation_rate = 0.25

def gen_chromosome():
    return [random.randint(0, num_machines - 1) for _ in range(num_jobs)]

def initialize_population():
    return [gen_chromosome() for _ in range(population_size)]

def cal_fitness(chromosome):
    machine_times = [0] * num_machines
    for job, machine in enumerate(chromosome):
        machine_times[machine] += processing_times[job]
    return 1 / max(machine_times)

def roulette_selection(population):
    total_fitness = sum(cal_fitness(chromo) for chromo in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chromo in population:
        current += cal_fitness(chromo)
        if current > pick:
            return chromo

def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(num_jobs), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def mutate(chromosome):
    if random.random() < mutation_rate:
        idx = random.randint(0, num_jobs - 1)
        chromosome[idx] = random.randint(0, num_machines - 1)

def genetic_algorithm():
    population = initialize_population()
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = roulette_selection(population), roulette_selection(population)
            child1, child2 = two_point_crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    
    best_solution = max(population, key=cal_fitness)
    return best_solution, 1 / cal_fitness(best_solution)

best_solution, best_time = genetic_algorithm()
print("Best Schedule:", best_solution)
print("Minimum Completion Time:", best_time)