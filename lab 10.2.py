import random

JOBS = 10
MACHINES = 5
POP_SIZE = 25
MAX_GENERATIONS = 12
CROSSOVER_PROB = 0.88
MUTATION_PROB = 0.18
JOB_TIMES = [10, 5, 15, 7, 12, 8, 14, 6, 9, 11]

def generate_solution():
    return [random.randint(0, MACHINES - 1) for _ in range(JOBS)]

def evaluate_fitness(schedule):
    machine_load = [0] * MACHINES
    for idx, machine in enumerate(schedule):
        machine_load[machine] += JOB_TIMES[idx]
    return 1 / max(machine_load)

def perform_crossover(parent1, parent2):
    if random.random() < CROSSOVER_PROB:
        pt1, pt2 = sorted(random.sample(range(JOBS), 2))
        offspring1 = parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]
        offspring2 = parent2[:pt1] + parent1[pt1:pt2] + parent2[pt2:]
        return offspring1, offspring2
    return parent1, parent2

def apply_mutation(schedule):
    return [random.randint(0, MACHINES - 1) if random.random() < MUTATION_PROB else gene for gene in schedule]

def run_genetic_algorithm():
    population = [generate_solution() for _ in range(POP_SIZE)]
    best_result = None
    highest_fitness = 0

    for gen in range(MAX_GENERATIONS):
        fitness_scores = [evaluate_fitness(ind) for ind in population]
        current_best_fitness = max(fitness_scores)

        if current_best_fitness > highest_fitness:
            highest_fitness = current_best_fitness
            best_result = population[fitness_scores.index(current_best_fitness)]

        next_gen = []
        while len(next_gen) < POP_SIZE:
            p1, p2 = random.choices(population, weights=fitness_scores, k=2)
            child1, child2 = perform_crossover(p1, p2)
            next_gen.extend([apply_mutation(child1), apply_mutation(child2)])

        population = next_gen[:POP_SIZE]

        print(f"Generation {gen + 1}: Best Fitness = {highest_fitness:.5f}")

    return best_result, highest_fitness

optimal_schedule, optimal_fitness = run_genetic_algorithm()
print("\nOptimal Schedule:", optimal_schedule)
print("Best Fitness (1 / Completion Time):", optimal_fitness)
print("Total Completion Time:", 1 / optimal_fitness)
