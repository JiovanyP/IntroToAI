import random

# Parameters
num_particles = 5
iterations = 5
w = 0.5  # inertia weight
c1 = 1   # cognitive coefficient
c2 = 2   # social coefficient

# Initialize particles
particles = [random.uniform(0, 31) for _ in range(num_particles)]
velocities = [random.uniform(-1, 1) for _ in range(num_particles)]
pBest = particles[:]
pBest_scores = [x**2 for x in particles]
gBest = max(zip(particles, pBest_scores), key=lambda t: t[1])[0]

# Fitness function
def fitness(x):
    return x**2

# PSO iterations
for i in range(iterations):
    for j in range(num_particles):
        r1, r2 = random.random(), random.random()
        velocities[j] = (w * velocities[j] +
                         c1 * r1 * (pBest[j] - particles[j]) +
                         c2 * r2 * (gBest - particles[j]))
        particles[j] += velocities[j]
        # Update personal best
        if fitness(particles[j]) > pBest_scores[j]:
            pBest[j] = particles[j]
            pBest_scores[j] = fitness(particles[j])
    # Update global best
    gBest = max(zip(pBest, pBest_scores), key=lambda t: t[1])[0]
    print(f"Iteration {i+1}: gBest = {gBest}, Fitness = {fitness(gBest)}")