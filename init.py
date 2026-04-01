### F1
def init_grid(dimx, dimy):
    
    # PURPOSE: Initialize an empty grid to run simulation on.
    # INPUTS:
        # dimx: length of x dimension
        # dimy: length of y dimension
    # OUTPUTS: An empty array of dimx x dimy
    # SIDE EFFECTS: None

    # import required libraries
    import numpy as np 

    return np.zeros((dimy, dimx), dtype=int)