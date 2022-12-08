from functools import reduce

class Grid:
    matrix = []

    def column(self, col):
        return [row[col] for row in self.matrix]

    def row(self, row):
        return self.matrix[row]

    #returns list of lines from point, starting at the point to the edge
    #[up, down, left, right]
    def get_sightlines(self, col, row):
        return  [
            grid.column(col)[:row][::-1],
            grid.column(col)[row+1:],
            grid.row(row)[:col][::-1],
            grid.row(row)[col+1:],
        ]

def is_vis(col, row, grid):
    val = grid.matrix[row][col]
    visible = map(lambda sight: val > max(sight, default=-1), grid.get_sightlines(col, row))
    return reduce(lambda a, b: a or b, visible)

def sight_dist(sightline, height):
    vis_line = list(map(lambda vis_height: vis_height >= height, sightline))
    return vis_line.index(True) + 1 if True in vis_line else len(vis_line)

def scenic_score(col, row, grid):
    val = grid.matrix[row][col]
    scores = map(lambda sight: sight_dist(sight, val), grid.get_sightlines(col, row))
    return reduce(lambda a, b: a * b, scores)

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