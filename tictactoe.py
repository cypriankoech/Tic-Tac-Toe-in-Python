# Tic Tac Toe in python

# importing random, used to select the first player at random
import random as rd

# describes a function that prints out the board
def printboard():
    global row1,positions1,row2,positions2,row3,positions3 
    print ("{}\t{}\n{}\t{}\n{}\t{}\n".format(row1,positions1,row2,positions2,row3,positions3))

# describes a function that resets the board and allows a player to choose their symbol either 'x' or 'o'  
def start():
    # global variables to contain the three rows and and present their positions alongside the board
    global row1,positions1,row2,positions2,row3,positions3,game_continuing,replay,turn,player,players
    row1 = list(['-','-','-'])
    positions1 = list([1,2,3])

    row2 = list(['-','-','-'])
    positions2 = list([4,5,6])

    row3 = list(['-','-','-'])
    positions3 = list([7,8,9])
    
    # resets game_continuing to true so us to allow the game to be played (True is required for the while loop to run)
    game_continuing=True
    
    # Gives the players a chance to replay the game once its over
    replay = True
    
    # first turn to be played starts undecided and is picked at random by the computer
    turn='None'
    
    # does not have to be 'x' and 'o', here an array with 2 random elements is created as place holders for player 1's and 2's chosen symbols
    players = ['x','o']
    
    #resets player_chosen to false to allow players to choose their symbols,will be set to True once first player is chosen
    player_chosen = False
    while not player_chosen:
        # user input requesting the first player to pick their symbol
        players[0] = input('Player 1 choose your symbol.\nHINT: Choose \'x\' or \'o\' ').lower()
        # if statement to choose the 2nd player's symbol by default, it also repeats the question in case a wrong input is typed in
        if players[0]=='x':
            players[1]='o'
            player_chosen = True
        elif players[0]=='o':
            players[1]='x'
            player_chosen = True
        else:
            print("\ninvalid input for player 1, please choose \'x\' or \'o\''")
# function to randomly decide who will be the first person to play
def firstplayer():
    global turn
    turn = rd.randint(0,1)
# This is function updates the board based on user input and displays the new board
def boardupdater():
    global row1,row2,row3,turn ,all_rows,player
    player = turn + 1
    printboard()
    
    # created a variable 'occupyable' it checks whether the player's selected position is available or taken
    occupyable = False
    while not occupyable:
        # Exception handling for ValueErrors, so ast to keep the game going and to notify the players that 
        # the input must be integral and between 1 and 10
        try:
            position = int(input("Player {}('{}') choose your position\n".format(player,players[turn])))
            # if statement which updates the board based on the position given by the player
            if position>0 and position<=9:
                if position>=0 and position<=3 and row1[position-1]=='-':
                        row1[position-1] = players[turn]
                        occupyable = True
                elif position>=4 and position<=6 and row2[position-4]=='-':
                        row2[position-4] = players[turn]
                        occupyable = True
                elif position>=7 and  position<=9 and row3[position-7]=='-':
                        row3[position-7] = players[turn]
                        occupyable = True
                else:
                    print("That position is already occupied")
                    occupyable = False
            else:
                print("That position is not within the board")
                occupyable = False
            # creates an array that stores all placed values, to be used for checking for a tie later
            all_rows = row1+row2+row3
        except ValueError:
            print("\nThe value inserted must be an INTEGER between and including 1 and 9")
            occupyable = False
    

# describes a function that checks the board for a winner once a player has placed their mark on the board
def winnerchecker():
    global game_continuing
    game_continuing=True
    # The first part of the if statement is meant to check the rows for a winner
    if (row1[0]==row1[1]==row1[2]!='-') or (row2[0]==row2[1]==row2[2]!='-') or (row3[0]==row3[1]==row3[2]!='-'):
        game_continuing=False
        printboard()
        print("The winner is Player {}('{}')".format(player,players[turn]))
    # This second part of the if statement is meant to check the columns for a winner
    elif(row1[0]==row2[0]==row3[0]!='-') or (row1[1]==row2[1]==row3[1]!='-') or (row1[2]==row2[2]==row3[2]!='-'):
        game_continuing=False
        printboard()
        print("The winner is Player {}('{}')".format(player,players[turn]))
    # This third part of the if statement is meant to check the diagonals for a winner
    elif(row1[0]==row2[1]==row3[2]!='-') or (row3[0]==row2[1]==row1[2]!='-'):
        game_continuing=False
        printboard()
        print("The winner is Player {}('{}')".format(player,players[turn]))
    # This fourth part of the if statement is meant to check for a tie, if all parts of the board are filled and 
    # there is no winner
    elif '-' not in all_rows:
        game_continuing=False
        printboard()
        print("No Winner. its a Tie")

# Describes a function that handles the turns, by switching the player after he/she has chosen their latest
# position on the board
def playerswitcher():
    global player ,turn
    if turn==0:
        turn=1       
    elif turn==1:
        turn=0
    player = turn + 1
    
 # Describes a function which allows the players to chose whether they want to play another match   
def replaychecker():
    global replay
    replay=True
    valid = False
    # While loop which determines whether the choice is valid, and allows the user to make a different one incase
    # the choice is invalid
    while not valid:
        choice = input("Do you wish to replay ?\n1.Yes\n2.No\n").lower()
        if choice=='1' or choice=='yes':
            valid = True
        elif choice=='2' or choice=='no':
            print('Bye...')
            valid=True
            replay=False
        else:
            print("Invalid choice. Please try again")

# Describes a function that plays the game
def play_game():
    try:
        global replay
        replay = True
        while replay:
            start()
            firstplayer()
            while game_continuing:
                boardupdater()
                winnerchecker()
                playerswitcher()
            replaychecker()
    # Exception handling to check if the player interrupts the program while running and reports when it occurs
    except KeyboardInterrupt:
        print("\nThe game has been stopped")
# runs the function to play the game        
play_game()
