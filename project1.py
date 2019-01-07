

def display_board(board):
    print('\n'*100)
    
    
    print('          '+board[7]+' |  '+board[8]+' |  '+board[9])
    
        
    print('     --------------------')
    
    

    print('          '+board[4]+' |  '+board[5]+' |  '+board[6])
    
    

                
    print('     --------------------')
    
    
    print('          '+board[1]+' |  '+board[2]+' |  '+board[3])

    
def player_input():
    
    player_1=input('Player 1 Enter x or o ').upper()
    
    
    while player_1!='X' and player_1!='O':
       
        player_1=input('Player 1 Enter X or o ').upper()
    
    if player_1=='X':
        
        player_2='O'
    
    else:
            player_2='X'
    
    return (player_1,player_2)


def place_marker1(board, marker, position):
    for i in marker:
        board[position]=i
def place_marker2(board, marker, position):
    for i in marker:
        board[position]=i


    
def win_check(board, mark):
    if  (board[1]==board[2]==board[3]==mark[0]
        or
        board[4]==board[5]==board[6]==mark[0]
        or
        board[7]==board[8]==board[9]==mark[0]
        or
        board[1]==board[5]==board[9]==mark[0]
        or
        board[3]==board[5]==board[7]==mark[0]
        or
        board[1]==board[4]==board[7]==mark[0]
        or
        board[2]==board[5]==board[8]==mark[0]
        or
        board[3]==board[6]==board[9]==mark[0]):
            
            return True
    elif (board[1]==board[2]==board[3]==mark[1]
        or
        board[4]==board[5]==board[6]==mark[1]
        or
        board[7]==board[8]==board[9]==mark[1]
        or
        board[1]==board[5]==board[9]==mark[1]
        or
        board[3]==board[5]==board[7]==mark[1]
        or
        board[1]==board[4]==board[7]==mark[1]
        or
        board[2]==board[5]==board[8]==mark[1]
        or
        board[3]==board[6]==board[9]==mark[1]):

            return True
def space_check(board, position):
    return board[position]==''
def full_board_check(board):
    for i in range(1,10):
            if space_check(board,i):
                return False
    return True
         
def replay():
    p=input("Do You Want to Play Again:")
    if p=='yes':
        return True
    else:
        return False







print('Welcome to Tic Tac Toe!')

while True:
    marker=player_input()
    test_board = ['']*10
    while full_board_check(test_board)==False:
        def player_choice(board):
            position=int(input("Enter Your Position 1-9:"))
            if space_check(test_board,position)==True:
                return position
            else:
                while space_check(test_board,position)==False:
                    position=int(input("Enter Correct Position:"))
                    return position
        #PlAYER 1 TURN
        position=player_choice(test_board)
        place_marker1(test_board,marker[0],position)
        display_board(test_board)
        win_check(test_board,marker)
        if win_check(test_board,marker)==True:
            print("Player 1 Has Won the Game")
            break
        else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('The game is a draw!')
                    break
        
        #PLAYER 2 TURN
        position=player_choice(test_board)
        place_marker2(test_board,marker[1],position)
        display_board(test_board)
        win_check(test_board,marker)
        if win_check(test_board,marker)==True:
            print('Player 2 Has Won The Game')
            break
        else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('The game is a draw!')
                    break
  
        
    if not replay():
            break
