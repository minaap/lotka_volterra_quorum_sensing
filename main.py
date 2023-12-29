# Main runner
# Basically, I want a separate program for running the Lotka-Volterra model.
# This program is just for deciding what goes in/out.

import numpy as np
import lotka_volterra as lv

population = np.array([100,200])
weights = np.array([[-0.01, 0.01],
                    [-0.1, 0.1]])
quorum_sensing = np.array([[]])

lv.sim(population, weights, quorum_sensing)

