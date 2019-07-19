'''
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
'''
#RETURNS BOOLEAN

def is_valid(state, player, row, column):
    if player=='B':
        other = 'W'
    if player=='W':
        other = 'B'
    new_state = [x[:] for x in state]       #copying the old state
    if(new_state[row][column]!=' '): return False       #if a spot is already occupied, return
    new_state[row][column] = player                 #place the tile for the player


    left_fliplist = []             #checking the left side of the placed tile
    i = column - 1
    end = 0
    while i >= 0 :
        if new_state[row][i] == other:
            left_fliplist.append((row, i))
        if new_state[row][i] == ' ':
            del left_fliplist[:]
            break
        if new_state[row][i] == player:
            end = 1
            break
        i = i - 1
    if end == 0:    # if there is no player color piece on the other end to sandwish the opponent pieces in between, nothing will be flipped
        del left_fliplist[:]
    i = 0
    for i in range(0, len(left_fliplist)):          #flipping the tiles to player's color
        new_state[left_fliplist[i][0]][left_fliplist[i][1]]=player


    right_fliplist = []       #checking the right side of the placed tile
    i = column + 1
    end = 0
    while i < len(new_state[row]):
        if new_state[row][i] == other:
            right_fliplist.append((row, i))
        if new_state[row][i] == ' ':
            del right_fliplist[:]
            break
        if new_state[row][i] == player:
            end = 1
            break
        i = i + 1
    if end == 0:
        del right_fliplist[:]
    i = 0
    for i in range(0, len(right_fliplist)):          #flipping the tiles to player's color
        new_state[right_fliplist[i][0]][right_fliplist[i][1]]=player


    up_fliplist = []          #checking the up side of the placed tile
    i = row -1
    end = 0
    while i>=0:
        if new_state[i][column] == other:
            up_fliplist.append((i, column))
        if new_state[i][column] == ' ':
            del up_fliplist[:]
            break
        if new_state[i][column] == player:
            end = 1
            break
        i=i-1
    if end==0:
        del up_fliplist[:]
    i = 0
    for i in range(0, len(up_fliplist)):  # flipping the tiles to player's color
        new_state[up_fliplist[i][0]][up_fliplist[i][1]] = player


    down_fliplist = []     #checking the down side of the placed tile
    i = row+1
    end = 0
    while i<len(new_state):
        if new_state[i][column] == other:
            down_fliplist.append((i, column))
        if new_state[i][column] == ' ':
            del down_fliplist[:]
            break
        if new_state[i][column] == player:
            end = 1
            break
        i=i+1
    if end==0:
        del down_fliplist[:]
    i = 0
    for i in range(0, len(down_fliplist)):  # flipping the tiles to player's color
        new_state[down_fliplist[i][0]][down_fliplist[i][1]] = player


    i = row-1                       #checking upper right side of the placed tile
    j = column+1
    end = 0
    upRight_fliplist = []
    while i>=0 and j<len(new_state[row]):
        if(new_state[i][j]==other):
            upRight_fliplist.append((i,j))
        if(new_state[i][j]==' '):
            del upRight_fliplist[:]
            break
        if(new_state[i][j]==player):
            end = 1
            break
        i=i-1
        j=j+1
    if(end ==0):
        del upRight_fliplist[:]
    i = 0
    for i in range(0, len(upRight_fliplist)):  # flipping the tiles to player's color
        new_state[upRight_fliplist[i][0]][upRight_fliplist[i][1]] = player


    i = row-1                   #checking upper left side of the placed tile
    j = column-1
    end = 0
    upLeft_fliplist = []
    while i >=0 and j >= 0:
        if (new_state[i][j] == other):
            upLeft_fliplist.append((i, j))
        if (new_state[i][j] == ' '):
            del upLeft_fliplist[:]
            break
        if (new_state[i][j] == player):
            end = 1
            break
        i = i-1
        j = j-1
    if (end == 0):
        del upLeft_fliplist[:]
    i = 0
    for i in range(0, len(upLeft_fliplist)):  # flipping the tiles to player's color
        new_state[upLeft_fliplist[i][0]][upLeft_fliplist[i][1]] = player


    i = row+1                   #checking lower right side of the placed tile
    j = column+1
    end = 0
    downRight_fliplist = []
    while i<len(new_state) and j<len(new_state[row]):
        if (new_state[i][j] == other):
            downRight_fliplist.append((i, j))
        if (new_state[i][j] == ' '):
            del downRight_fliplist[:]
            break
        if (new_state[i][j] == player):
            end = 1
            break
        i = i+1
        j = j+1
    if(end ==0):
        del downRight_fliplist[:]
    i = 0
    for i in range(0, len(downRight_fliplist)):  # flipping the tiles to player's color
        new_state[downRight_fliplist[i][0]][downRight_fliplist[i][1]] = player


    i = row+1                   #checking lower left side of the placed tile
    j = column-1
    end = 0
    downLeft_fliplist = []
    while i<len(new_state) and j >= 0:
        if new_state[i][j] == other:
            downLeft_fliplist.append((i, j))
        if (new_state[i][j] == ' '):
            del downLeft_fliplist[:]
            break
        if (new_state[i][j] == player):
            end = 1
            break
        i = i+1
        j = j-1
    if(end==0):
        del downLeft_fliplist[:]
    i = 0
    for i in range(0, len(downLeft_fliplist)):  # flipping the tiles to player's color
        new_state[downLeft_fliplist[i][0]][downLeft_fliplist[i][1]] = player

    if(len(right_fliplist)+len(left_fliplist)+len(up_fliplist)+len(down_fliplist)+len(upLeft_fliplist)+len(upRight_fliplist)+len(downLeft_fliplist)+len(downRight_fliplist) == 0):
        return False
    return True

#RETURNS INT
def get_move_value(state, player, row, column):
    flipped = 0
    # Your implementation goes here
    p=1
    if(player == 'W'): p=0
    if(is_valid(state, player, row, column) == False):
        return 0
    temp = [x[:] for x in state]
    if(temp[row][column]!= ' '): return 0
    flipped = count_pieces(state)[p]-count_pieces(execute_move(temp, player, row, column))[p]

    return flipped


'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 

RETURNS TYPE STATE
'''
def execute_move(state, player, row, column):
    new_state = None
    # Your implementation goes here
    if player=='B':
        other = 'W'
    if player=='W':
        other = 'B'

    new_state = [x[:] for x in state]       #copying the old state
    if(new_state[row][column]!=' '): return state       #if a spot is already occupied, return
    new_state[row][column] = player                 #place the tile for the player


    left_fliplist = []             #checking the left side of the placed tile
    i = column - 1
    end = 0
    while i >= 0 :
        if new_state[row][i] == other:
            left_fliplist.append((row, i))
        if new_state[row][i] == ' ':
            del left_fliplist[:]
            break
        if new_state[row][i] == player:
            end = 1
            break
        i = i - 1
    if end == 0:    # if there is no player color piece on the other end to sandwish the opponent pieces in between, nothing will be flipped
        del left_fliplist[:]
    i = 0
    for i in range(0, len(left_fliplist)):          #flipping the tiles to player's color
        new_state[left_fliplist[i][0]][left_fliplist[i][1]]=player


    right_fliplist = []       #checking the right side of the placed tile
    i = column + 1
    end = 0
    while i < len(new_state[row]):
        if new_state[row][i] == other:
            right_fliplist.append((row, i))
        if new_state[row][i] == ' ':
            del right_fliplist[:]
            break
        if new_state[row][i] == player:
            end = 1
            break
        i = i + 1
    if end == 0:
        del right_fliplist[:]
    i = 0
    for i in range(0, len(right_fliplist)):          #flipping the tiles to player's color
        new_state[right_fliplist[i][0]][right_fliplist[i][1]]=player


    up_fliplist = []          #checking the up side of the placed tile
    i = row -1
    end = 0
    while i>=0:
        if new_state[i][column] == other:
            up_fliplist.append((i, column))
        if new_state[i][column] == ' ':
            del up_fliplist[:]
            break
        if new_state[i][column] == player:
            end = 1
            break
        i=i-1
    if end==0:
        del up_fliplist[:]
    i = 0
    for i in range(0, len(up_fliplist)):  # flipping the tiles to player's color
        new_state[up_fliplist[i][0]][up_fliplist[i][1]] = player


    down_fliplist = []     #checking the down side of the placed tile
    i = row+1
    end = 0
    while i<len(new_state):
        if new_state[i][column] == other:
            down_fliplist.append((i, column))
        if new_state[i][column] == ' ':
            del down_fliplist[:]
            break
        if new_state[i][column] == player:
            end = 1
            break
        i=i+1
    if end==0:
        del down_fliplist[:]
    i = 0
    for i in range(0, len(down_fliplist)):  # flipping the tiles to player's color
        new_state[down_fliplist[i][0]][down_fliplist[i][1]] = player


    i = row-1                       #checking upper right side of the placed tile
    j = column+1
    end = 0
    upRight_fliplist = []
    while i>=0 and j<len(new_state[row]):
        if(new_state[i][j]==other):
            upRight_fliplist.append((i,j))
        if(new_state[i][j]==' '):
            del upRight_fliplist[:]
            break
        if(new_state[i][j]==player):
            end = 1
            break
        i=i-1
        j=j+1
    if(end ==0):
        del upRight_fliplist[:]
    i = 0
    for i in range(0, len(upRight_fliplist)):  # flipping the tiles to player's color
        new_state[upRight_fliplist[i][0]][upRight_fliplist[i][1]] = player


    i = row-1                   #checking upper left side of the placed tile
    j = column-1
    end = 0
    upLeft_fliplist = []
    while i >=0 and j >= 0:
        if (new_state[i][j] == other):
            upLeft_fliplist.append((i, j))
        if (new_state[i][j] == ' '):
            del upLeft_fliplist[:]
            break
        if (new_state[i][j] == player):
            end = 1
            break
        i = i-1
        j = j-1
    if (end == 0):
        del upLeft_fliplist[:]
    i = 0
    for i in range(0, len(upLeft_fliplist)):  # flipping the tiles to player's color
        new_state[upLeft_fliplist[i][0]][upLeft_fliplist[i][1]] = player


    i = row+1                   #checking lower right side of the placed tile
    j = column+1
    end = 0
    downRight_fliplist = []
    while i<len(new_state) and j<len(new_state[row]):
        if (new_state[i][j] == other):
            downRight_fliplist.append((i, j))
        if (new_state[i][j] == ' '):
            del downRight_fliplist[:]
            break
        if (new_state[i][j] == player):
            end = 1
            break
        i = i+1
        j = j+1
    if(end ==0):
        del downRight_fliplist[:]
    i = 0
    for i in range(0, len(downRight_fliplist)):  # flipping the tiles to player's color
        new_state[downRight_fliplist[i][0]][downRight_fliplist[i][1]] = player


    i = row+1                   #checking lower left side of the placed tile
    j = column-1
    end = 0
    downLeft_fliplist = []
    while i<len(new_state) and j >= 0:
        if new_state[i][j] == other:
            downLeft_fliplist.append((i, j))
        if (new_state[i][j] == ' '):
            del downLeft_fliplist[:]
            break
        if (new_state[i][j] == player):
            end = 1
            break
        i = i+1
        j = j-1
    if(end==0):
        del downLeft_fliplist[:]
    i = 0
    for i in range(0, len(downLeft_fliplist)):  # flipping the tiles to player's color
        new_state[downLeft_fliplist[i][0]][downLeft_fliplist[i][1]] = player

    if(len(right_fliplist)+len(left_fliplist)+len(up_fliplist)+len(down_fliplist)+len(upLeft_fliplist)+len(upRight_fliplist)+len(downLeft_fliplist)+len(downRight_fliplist) == 0):
        print "invalid move"
        return state

    return new_state

'''
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpieces, white pieces), e.g.,

    return (4, 3)

'''
def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            if state[i][j]=='B':
                blackpieces = blackpieces+1
            if state[i][j]=='W':
                whitepieces = whitepieces+1
    # Your implementation goes here 
    return (blackpieces, whitepieces)

'''
Check whether a state is a terminal state. 
'''
def is_terminal_state(state, state_list = None):
    # Your implementation goes here 
    terminal = True
    for i in range(0, len(state)):
        for j in range(0, len(state)):
            if (is_valid(state, 'B', i, j) == True):
                return False
            if (is_valid(state, 'W', i, j) == True):
                return False
    return terminal
def is_terminal_statew(state, state_list = None):
    # Your implementation goes here
    terminal = True
    for i in range(0, len(state)):
        for j in range(0, len(state)):
            if (is_valid(state, 'W', i, j) == True):
                return False
    return terminal
def is_terminal_stateb(state, state_list = None):
    # Your implementation goes here
    terminal = True
    for i in range(0, len(state)):
        for j in range(0, len(state)):
            if (is_valid(state, 'B', i, j) == True):
                return False
    return terminal
'''
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
'''
def minimax(state, player):
    #print
    #print "another RUN!"
    value1 = -10000
    value2 = 10000
    row = -1
    column = -1
    # Your implementation goes here

    if player=='B':
        other = 'W'
    else:
        other = 'B'
    #case 1: current move is a terminal state


    if(is_terminal_statew(state, None) == True and is_terminal_stateb(state, None) == True):
        #print "TERMINAL STATE!!!!"
        tup = count_pieces(state)
        temp_value = tup[0] - tup[1]
        if (player == 'B'):
            if (temp_value > value1):
                value1 = temp_value
        if (player == 'W'):
            if (temp_value < value2):
                value2 = temp_value




    else:
        #print("not terminal state")
        for i in range(0, len(state)):
            for j in range(0, len(state)):
                #case 0: move is not valid
                if (is_valid(state, player, i, j) == True):
                    temp_state = execute_move(state, player, i, j)
                    #print "current player is: "+player
                    #for g in range(0, len(temp_state)):
                    #    print temp_state[g]

                    #print
                    #case 2: current move is not a terminal state


                    tup2 = None
                    if(player == 'W' and is_terminal_stateb(temp_state, None) == True):
                       # print"running another minimax on that temp_state with white player"
                        tup2 = minimax(temp_state, 'W')
                    elif (player == 'B' and is_terminal_statew(temp_state, None) == True):
                      #  print"running another minimax on that temp_state with Black player"
                        tup2 = minimax(temp_state, 'B')
                    else:
                      #  print"running another minimax on that temp_state with other player"
                        tup2 = minimax(temp_state, other)
                    if tup2!=None:
                        if ((player == 'B') and (tup2[0] > value1)):
                        #    print "player is black"
                       #     print "value1 is"+str(value1)
                      #      print "tup2[0] is"+str(tup2[0])
                            value1 = tup2[0]
                            row = i
                            column = j
                        if ((player == 'W') and (tup2[0] < value2)):
                        #    print "player is white"
                        #    print "value2 is" + str(value2)
                        #    print "tup2[0] is" + str(tup2[0])
                            value2 = tup2[0]
                            row = i
                            column = j
    #print "neither"
    if (player == 'B'):
        #print "end player is black"
       # print "value1 is: "+str(value1)
        #print
        return (value1, row, column)
    if (player == 'W'):
       # print "end player is white"
       # print "value2 is: " + str(value2)
       # print
        return (value2, row, column)







    '''
    for i in range(0, len(state)):
        for j in range(0, len(state)):
            if (get_move_value(state, player, i, j) > value):
                row = i
                column = j
    tup = count_pieces(execute_move(state, player, row, column))
    print 1
    value = tup[0] - tup[1]
    return (value, row, column)
    '''

'''
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
'''
def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    
    
    current_player = player
    new_state = [x[:] for x in state]
    while(is_terminal_state(new_state, None) == False):
        if current_player=='B':
            other = 'W'
        if current_player=='W':
            other = 'B'
        temp = minimax(new_state, current_player)
        move_sequence.append((current_player, temp[1], temp[2]))
        new_state = execute_move(new_state, current_player, temp[1], temp[2])
        current_player = other
    move_sequence.append((current_player, -1, -1))
    tup = count_pieces(new_state)
    value = tup[0] - tup[1]
    return (value, move_sequence)
    


'''
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
'''
def minimax_ab(state, player, alpha = -10000000, beta = 10000000):
    value1 = -10000
    value2 = 10000
    row = -1
    column = -1
    # Your implementation goes here

    if player=='B':
        other = 'W'
    else:
        other = 'B'
    #case 1: current move is a terminal state


    if(is_terminal_statew(state, None) == True and is_terminal_stateb(state, None) == True):
        #print "TERMINAL STATE!!!!"
        tup = count_pieces(state)
        temp_value = tup[0] - tup[1]
        if (player == 'B'):
            if (temp_value > value1):
                value1 = temp_value
        if (player == 'W'):
            if (temp_value < value2):
                value2 = temp_value




    else:
        #print("not terminal state")
        for i in range(0, len(state)):
            for j in range(0, len(state)):
                #case 0: move is not valid
                if (is_valid(state, player, i, j) == True):
                    temp_state = execute_move(state, player, i, j)
                    print "current player is: "+player
                    for g in range(0, len(temp_state)):
                       print temp_state[g]

                    #print
                    #case 2: current move is not a terminal state


                    tup2 = None
                    if(player == 'W' and is_terminal_stateb(temp_state, None) == True):
                       # print"running another minimax on that temp_state with white player"
                        tup2 = minimax_ab(temp_state, 'W')
                    elif (player == 'B' and is_terminal_statew(temp_state, None) == True):
                      #  print"running another minimax on that temp_state with Black player"
                        tup2 = minimax_ab(temp_state, 'B')
                    else:
                      #  print"running another minimax on that temp_state with other player"
                        tup2 = minimax_ab(temp_state, other)
                    if tup2!=None:
                        if ((player == 'B') and (tup2[0] > value1)):
                        #    print "player is black"
                       #     print "value1 is"+str(value1)
                      #      print "tup2[0] is"+str(tup2[0])
                            value1 = tup2[0]
                            if value1>alpha:
                                alpha = value1
                            row = i
                            column = j
                            if alpha >= beta:
                                return (value1, row, column)
                        if ((player == 'W') and (tup2[0] < value2)):
                        #    print "player is white"
                        #    print "value2 is" + str(value2)
                        #    print "tup2[0] is" + str(tup2[0])
                            value2 = tup2[0]
                            if value2>beta:
                                beta = value2    
                            row = i
                            column = j
                            if alpha <= beta:
                                return (value2, row, column)
    #print "neither"
    if (player == 'B'):
        #print "end player is black"
       # print "value1 is: "+str(value1)
        #print
        return (value1, row, column)
    if (player == 'W'):
       # print "end player is white"
       # print "value2 is: " + str(value2)
       # print
        return (value2, row, column)

'''
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
'''
def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here 
    current_player = player
    new_state = [x[:] for x in state]
    while(is_terminal_state(new_state, None) == False):
        if current_player=='B':
            other = 'W'
        if current_player=='W':
            other = 'B'
        temp = minimax_ab(new_state, current_player)
        move_sequence.append((current_player, temp[1], temp[2]))
        new_state = execute_move(new_state, current_player, temp[1], temp[2])
        current_player = other
    move_sequence.append((current_player, -1, -1))
    tup = count_pieces(new_state)
    value = tup[0] - tup[1]
    return (value, move_sequence)


