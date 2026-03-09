import random

# Parameters
num_particles = 5
iterations = 5
w, c1, c2 = 0.5, 1, 2

# Initialize particles
particles = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(num_particles)]
velocities = [[random.uniform(-1,1), random.uniform(-1,1)] for _ in range(num_particles)]
pBest = [p[:] for p in particles]
pBest_scores = [p[0]**2 + p[1]**2 for p in particles]
gBest = min(zip(particles, pBest_scores), key=lambda t: t[1])[0]

# Fitness function
def fitness(pos):
    return pos[0]**2 + pos[1]**2

# PSO iterations
for i in range(iterations):
    for j in range(num_particles):
        for d in range(2):
            r1, r2 = random.random(), random.random()
            velocities[j][d] = (w * velocities[j][d] +
                                c1 * r1 * (pBest[j][d] - particles[j][d]) +
                                c2 * r2 * (gBest[d] - particles[j][d]))
            particles[j][d] += velocities[j][d]
        # Update personal best
        if fitness(particles[j]) < pBest_scores[j]:
            pBest[j] = particles[j][:]
            pBest_scores[j] = fitness(particles[j])
    # Update global best
    gBest = min(zip(pBest, pBest_scores), key=lambda t: t[1])[0]
    print(f"Iteration {i+1}: gBest = {gBest}, Fitness = {fitness(gBest)}")