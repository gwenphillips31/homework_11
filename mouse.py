### F4

def mouse_to_cell(pos, cellsize):
    # PURPOSE: Use mouse to indicate cell position in grid
    # INPUTS: 
        # pos: position of mouse
        # cellsize: size of cell on pydata interactive grid
    # OUTPUTS: Returns the cell that was activated by the mouse
    # SIDE EFFECTS: None
    x, y = pos
    return y // cellsize, x // cellsize