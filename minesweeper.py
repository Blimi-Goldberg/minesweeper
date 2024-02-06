# reading the matrix from text file and splitting it by each row
with open("input.txt", "r") as file:
    grid = file.read().split("], ")
    print(grid)

num_rows = len(grid)
num_cols = len(grid[0].split(","))
# creating a new empty grid for my input 
my_input = [[None] * num_cols for i in range(num_rows)]
my_grid = [[None] * num_cols for i in range(num_rows)]
for x, row in enumerate(grid):
    my_row = row.split(",")
    for y, col in enumerate(my_row):
        my_input[x][y] = col
# use a nested for loop to figure out where the mines are and add 1 if there is a mine around it        
for x, row in enumerate(my_input):
    for y, col in enumerate(row):
        if col.find("#") != -1:
            my_grid[x][y] = "#"
        elif col.find("-") != -1:
            num_mines = 0
            # creating boundaries 
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < num_rows and 0 <= j < num_cols:
                        if my_input[i][j].find("#") != -1:
                            num_mines += 1

            my_grid[x][y] = str(num_mines)

for row in my_grid:
    print(row)


