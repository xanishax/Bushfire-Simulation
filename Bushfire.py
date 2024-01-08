#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name of student: Anisha Mariam Abraham
Student ID: 110416080
Course Name: COMP5070 - Statistical Programming for Data Science
"""
import random as rd

# LIMIT denotes the size of the forest in one dimension. Since the forest is a
# perfect square, the size of the forest is LIMIT^2.
# DENSITY notes the proportion of trees in the forest.
# full_trees gives the number of trees in the forest calculated from the density
# and size.
# All variables and functions have been named following the naming conventions.

LIMIT = 10
DENSITY = 0.7
SIMULATIONS = 1000

full_trees = int(DENSITY * LIMIT * LIMIT)

forest = []
sum_steps = 0
sum_healthy_trees = 0


# Functions

def create_forest():

    # This function is for creating forest.
    # Every cell in the forest is assumed to be 'E'mpty initially.

    forest = [['E' for i in range(LIMIT)] for j in range(LIMIT)]
    return forest


def assign_density(forest):

    # This function is to assign the required density to the forest.
    # For example if density is 0.3, 30% of the forest will have trees.
    # full_trees calculates the number of trees for a particular forest
    # with given density.

    for i in range(full_trees):
            random_row, random_col = rd.randint(0,LIMIT-1),rd.randint(0,LIMIT-1)
            forest[random_row][random_col] = 'F'


def start_bushfire(forest):

    # This function starts a bushfire 'T' at a single random cell, provided the
    # cell has a tree ie 'F'.

    while(True):
        random_row, random_col = rd.randint(0,LIMIT-1),rd.randint(0,LIMIT-1)
        if forest[random_row][random_col] == 'F':
            forest[random_row][random_col] = 'T'
            break;


def spread_fire(forest):

    # This function spreads the fire 'T' to the neighbouring
    # cells if there is a tree 'F' in those cells. A new_forest is created to
    # store the current state and the updated forest is returned.


    # The length of fire from starting point (single 'T') to burn maximum trees
    # is counted by steps variable. The 'while' loop runs till there is no
    # change to the forest and all fire has burnt out. The number of healthy
    # trees at the end of this process is noted. The updated forest, total
    # length of the fire and number of healthy trees remaining are returned.

    new_forest = [['E' for _ in range(LIMIT)] for _ in range(LIMIT)]
    steps = 0

    while True:
        changed = False

        for i in range(LIMIT):
            for j in range(LIMIT):
                if forest[i][j] == 'T':
                    new_forest[i][j] = 'E'
                    changed = True

                elif forest[i][j] == 'F':
                    if any(
                        forest[x][y] == 'T'
                        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                        if 0 <= x < LIMIT and 0 <= y < LIMIT
                    ):
                        new_forest[i][j] = 'T'
                        changed = True
                    else:
                        new_forest[i][j] = 'F'

                else:
                    new_forest[i][j] = 'E'

        if not changed:
            break

        steps += 1
        forest = [[new_forest[i][j] for j in range(LIMIT)] for i in range(LIMIT)]

    healthy_trees = sum(row.count('F') for row in forest)

    return forest, steps, healthy_trees


def run_simulation():

    # This function runs one entire simulation of expected behaviour:
    # create forest, assign density, start fire at a random point and spread it.
    # The total length of the fire and number of healthy trees remaining are
    # returned.

    forest = create_forest()
    assign_density(forest)
    start_bushfire(forest)
    result_forest, steps, healthy_trees = spread_fire(forest)

    return steps, healthy_trees


# MAIN

# Repeat for the fixed number of simulations and get a summation of length of
# fire and healthy trees remaining.

for i in range(SIMULATIONS):
    steps, healthy_trees = run_simulation()
    sum_steps += steps
    sum_healthy_trees += healthy_trees

# Calculate the average length of fire and average healthy trees remaining.

mean_steps = sum_steps / SIMULATIONS
mean_healthy_trees = sum_healthy_trees / SIMULATIONS

print("Density for forest:", DENSITY)
print("Size of forest:", LIMIT, "x", LIMIT)
print("Average length of bushfire:", mean_steps)
print("Average number of healthy trees to survive:", int(mean_healthy_trees), "trees")


"""
Below is the table for analysing the trend for forests of sizes 100, 70, 50, 30
and 10 with different densities like 0.3, 0.5, 0.7 and 0.9.

|————————————————————————————————————————————————-——————————————————————————————|
| Size | Density | 	Average length of fire | Average n(healthy trees) to survive|
|———————————————————————————————————————————————————————————————————————-———————|
| 100 |	   0.3   |           2.8           |                2588                |
| 100 |	   0.5   |          5.925          |                3924                |
| 100 |	   0.7   |         17.623          |                4974                |
| 100 |	   0.9   |         124.387         |                4264                |
|—————————————————————————————————————————————-—————————————————————————————————|
|  70 |	   0.3   |          2.758          |                1266                |
|  70 |	   0.5   |          5.865          |                1917                |
|  70 |	   0.7   |         16.132          |                2414                |
|  70 |	   0.9   |         83.209          |                2057                |
|———————————————————————————————————————————————————-———————————————————————————|
|  50 |	   0.3   |          2.738          |                644                 |
|  50 |	   0.5   |          5.627          |                973                 |
|  50 |	   0.7   |         14.907          |                1214                |
|  50 |	   0.9   |         60.095          |                997                 |
|———————————————————————————————————————————————————-———————————————————————————|
|  30 |	   0.3   |          2.758          |                230                 |
|  30 |	   0.5   |          5.536          |                344                 |
|  30 |	   0.7   |         13.647          |                414                 |
|  30 |	   0.9   |         35.715          |                332                 |
|———————————————————————————————————————————————————————————————————————————————|
|  10 |	   0.3   |          2.482          |                23                  |
|  10 |	   0.5   |          4.196          |                32                  |
|  10 |	   0.7   |          7.387          |                35                  |
|  10 |	   0.9   |         11.236          |                29                  |
|——————————————————————————————————————————————————-————————————————————————————|

It can be observed that for a given size at a time, as the density increases,
the average length of the bushfire also increases. The average number of healthy
trees to survive also increases but when the forest reaches maximum density
(0.9), the number of healthy trees drops.


Tree density (0.3, 0.5, 0.7, 0.9) influences the average length of fire.
Higher tree density seems to lead to longer fire lengths. It also implies that
longer fires seem to be associated with fewer surviving healthy trees. Generally,
larger areas seem to have more surviving healthy trees. Hence, it appears that
moderate tree density (0.5, 0.7) leads to better tree survival.



"""



