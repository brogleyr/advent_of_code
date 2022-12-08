
class Grid:
    matrix = []

    def column(self, col):
        return [row[col] for row in self.matrix]

    def row(self, row):
        return self.matrix[row]

def is_vis(col, row, grid):
    val = grid.matrix[row][col]
    up = val > max(grid.column(col)[:row], default=-1)
    down = val > max(grid.column(col)[row+1:], default=-1)
    left = val > max(grid.row(row)[:col], default=-1)
    right = val > max(grid.row(row)[col+1:], default=-1)
    return up or down or left or right

def sight_dist(sightline, height):
    vis_line = list(map(lambda vis_height: vis_height >= height, sightline))
    #print(vis_line)
    if vis_line:
        return vis_line.index(True) + 1 if True in vis_line else len(vis_line)
    else:
        return 0

def scenic_score(col, row, grid):
    val = grid.matrix[row][col]
    #print(col, row, val)
    up = sight_dist(grid.column(col)[:row][::-1], val)
    down = sight_dist(grid.column(col)[row+1:], val)
    left = sight_dist(grid.row(row)[:col][::-1], val)
    right = sight_dist(grid.row(row)[col+1:], val)
    return up * down * left * right

lines = open('input.txt', 'r').readlines()
grid = Grid()
for line in lines:
    grid.matrix.append([int(dig) for dig in line.strip()])

visible = 0
scenic = []
for i in range(len(grid.matrix[0])):
    for j in range(len(grid.matrix)):
        if is_vis(i, j, grid): visible += 1
        scenic.append(scenic_score(i, j, grid))
print(visible)
print(max(scenic))