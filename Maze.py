#import GridViewer
import Viewer

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4
    
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

if __name__ == "__main__":
    grid = [
        [ WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
        [START, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, WALL],
        [ WALL,  WALL,  WALL,  WALL, EMPTY,  WALL, EMPTY,  WALL, EMPTY, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY, EMPTY, EMPTY, WALL],
        [ WALL,  WALL, EMPTY,  WALL,  WALL, EMPTY, EMPTY,  WALL, EMPTY, WALL],
        [ WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL,  WALL, EMPTY,  END],
        [ WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
    ]
    Viewer.view(grid) 
    #Viewer.view(grid)               
    #for i in range(len(grid)):
    #    for j in range(len(grid[i])):
    #        
    #        if grid[i][j] == EMPTY:
    #            print("  ", end = "")
    #                
    #        elif grid[i][j] == WALL:
    #            print("##", end = "")
    #                
    #        elif grid[i][j] == START:
    #            print("^^", end = "")
    #                
    #        elif grid[i][j] == END:
    #            print("$$", end = "")
    #                
    #        elif grid[i][j] == VISITED:
    #            print("..", end = "")
    #                
    #        else:
    #            raise AssertionError
    #        
    #    print()


    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    currentRow = 1
    currentCol = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(currentRow) + ", " + str(currentCol) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            currentRow -= 1
            
        elif direction == EAST:
            currentCol += 1
                
        elif direction == SOUTH:
            currentRow += 1
                
        elif direction == WEST:
            currentCol -= 1
        
        else:
            #print("MESSAGE 1") # Invalid direction.
            print("You have no idea where you're going.")         # MESSAGE 1
            
        if (currentRow < 0 or currentCol < 0 
                        or currentRow >= len(grid) 
                        or currentCol >= len(grid[currentRow])):
            done = True
            print("You fall into the chasm of doom.")             # MESSAGE 2
            #print("MESSAGE 2") # Out of bounds.
            
        else:
            if grid[currentRow][currentCol] == EMPTY:
                grid[currentRow][currentCol] = VISITED
                
            elif grid[currentRow][currentCol] == WALL:
                done = True
                print("You stumble blindly into a solid concrete wall.")  # MESSAGE 3
                #print("MESSAGE 3") # Hit wall.

            elif grid[currentRow][currentCol] == END:
                done = True
                solved = True
                print("SOLVED!")                                      # MESSAGE 4
                #print("MESSAGE 4") # Solved.
                
            else:
                pass # Do nothing
        
        charIndex += 1
    # end-while


    if not solved:
        print("You have failed to escape. Future archaeologists gaze upon your remains in bafflement.")  # MESSAGE 5
        #print("MESSAGE 5") # Did not reach the end.
    Viewer.view(grid) 
    #Viewer.view(grid)
    #for i in range(len(grid)):
    #    for j in range(len(grid[i])):
    #        
    #        if grid[i][j] == EMPTY:
    #            print("  ", end = "")
    #                
    #        elif grid[i][j] == WALL:
    #            print("##", end = "")
    #                
    #        elif grid[i][j] == START:
    #            print("^^", end = "")
    #                
    #        elif grid[i][j] == END:
    #            print("$$", end = "")
    #                
    #        elif grid[i][j] == VISITED:
    #            print("..", end = "")
    #                
    #        else:
    #            raise AssertionError
    #        
    #    print()
