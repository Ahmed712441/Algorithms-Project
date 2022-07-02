dp=[]
pegs_final=[]

def createArray(n):
    return [1] * n

def solvePuzzle(array):
    
    global dp ,pegs_final
    
    if (array,"Solved") in dp:
        return True

    
    if (array,"Unsolvable") in dp:
        return False

    
    if goalTest(array):
        pegs_final.append(array.index(1)+1)  
        return True

    moves = []
    for i in range(len(array)):
        if i < len(array) - 2:
            if array[i] == 1 and array[i + 1] == 1 and array[i + 2] == 0:
                moves.append((i, 'right'))
        if i > 1:
            if array[i] == 1 and array[i - 1] == 1 and array[i - 2] == 0:
                moves.append((i, 'left'))
    
    solved = False
    for move in moves:
        newArray = createNewConfig(array, move)
        if solvePuzzle(newArray):
            
            dp.append((newArray,"Solved"))
            solved = True    
        else:
            
            dp.append((newArray,"Unsolvable"))
        
    return solved

def createNewConfig(oldConfig, move):
    index, direction = move
    newConfig = [element for element in oldConfig]
    if direction == 'right':
        newConfig[index] = 0
        newConfig[index + 1] = 0
        newConfig[index + 2] = 1
    elif direction == 'left':
        newConfig[index] = 0
        newConfig[index - 1] = 0
        newConfig[index - 2] = 1
    return newConfig

def goalTest(array):
    if sum(array) == 1:
        return True
    return False

def getInitialHoles(board):
    indices = []
    for i in range(len(board)):
        b = [element for element in board]
        b[i] = 0
        if solvePuzzle(b):
            indices.append(i + 1)
    return indices

n = input('Enter number of pegs\n')
possible_solutions = getInitialHoles(createArray(int(n)))

print('there is possible solutions when hole is placed in :' ,possible_solutions)

print('final possible places for pegs :' ,pegs_final)

print('All_States:')
print(dp)