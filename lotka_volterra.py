#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: mjm
"""

import numpy as np

# Population is a list. Weights are an array with each row corresponding to
# a species. The quorum_sensing array simpy gives the switching population
# value followed by the new weights, with one species per row.
def sim(population: np.array, weights: np.array, quorum_sensing: np.array):
    print(population)
    
