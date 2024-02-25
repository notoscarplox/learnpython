grid = [['.', '.', '.', '.', '.', '.'],
 		['.', 'O', 'O', '.', '.', '.'],
 		['O', 'O', 'O', 'O', '.', '.'],
 		['O', 'O', 'O', 'O', 'O', '.'],
 		['.', 'O', 'O', 'O', 'O', 'O'],
 		['O', 'O', 'O', 'O', 'O', '.'],
 		['O', 'O', 'O', 'O', '.', '.'],
 		['.', 'O', 'O', '.', '.', '.'],
 		['.', '.', '.', '.', '.', '.']]

# grid = [["O", "O"],
# 		["X", "X"],
# 		["O", "X"]]

for j in range(len(grid[0])):
	for i in range(len(grid)):
		if i == len(grid) - 1:
			print(grid[i][j])
		else:
			print(grid[i][j], end=" ")





# print(grid[1][0], end=" ")
# print(grid[0][0],)
# print(grid[1][1], end=" ")
# print(grid[0][1], end=" ")


