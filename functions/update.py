### F3
def update_sir(grid, beta, gamma, S, I, R):
    # PURPOSE: Update the grid each time step based on rules
    # INPUTS: 
        # grid: previous grid
        # beta: transmission rate
        # gamma: recovery rate
        # S, I, R: numeric states for each class (S = 0, I = 1, R = 2)
    # OUTPUTS: New updated grid as a np array.
    # SIDE EFFECTS: None
    
    import numpy as np # required libary
    
    infected_neighbors = (
        np.roll(np.roll(grid == I, 1, 0), 1, 1) +
        np.roll(np.roll(grid == I, 1, 0), 0, 1) +
        np.roll(np.roll(grid == I, 1, 0), -1, 1) +
        np.roll(np.roll(grid == I, 0, 0), 1, 1) +
        np.roll(np.roll(grid == I, 0, 0), -1, 1) +
        np.roll(np.roll(grid == I, -1, 0), 1, 1) +
        np.roll(np.roll(grid == I, -1, 0), 0, 1) +
        np.roll(np.roll(grid == I, -1, 0), -1, 1)
    )

    new_grid = grid.copy()

    infect_prob = 1 - (1 - beta) ** infected_neighbors
    rand = np.random.rand(*grid.shape)

    new_grid[(grid == S) & (rand < infect_prob)] = I

    recover = (grid == I) & (np.random.rand(*grid.shape) < gamma)
    new_grid[recover] = R

    return new_grid