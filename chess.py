import pygame
pygame.init()

# setting up base for game
WIDTH = 750
HEIGHT = 602
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Manobhav is GOAT')
font = pygame.font.Font('freesansbold.ttf', 20)
timer = pygame.time.Clock()
fps = 60
black_moves = []
white_moves = []
cross_white = False
cross_black = False
promotion = False

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

# useful variables
captured_pieces_white = []
captured_pieces_black = []
left_castling_white = True
right_castling_white = True
left_castling_black = True
right_castling_black = True
check_black = False
check_white = False
white_promotion = False

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 69
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (60, 60))
black_queen_small = pygame.transform.scale(black_queen, (34, 34))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (60, 60))
black_king_small = pygame.transform.scale(black_king, (34, 34))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (60, 60))
black_rook_small = pygame.transform.scale(black_rook, (34, 34))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (60, 60))
black_bishop_small = pygame.transform.scale(black_bishop, (34, 34))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (60, 60))
black_knight_small = pygame.transform.scale(black_knight, (34, 34))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (48, 48))
black_pawn_small = pygame.transform.scale(black_pawn, (34, 34))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (60, 60))
white_queen_small = pygame.transform.scale(white_queen, (34, 34))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (60, 60))
white_king_small = pygame.transform.scale(white_king, (34, 34))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (60, 60))
white_rook_small = pygame.transform.scale(white_rook, (34, 34))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (60, 60))
white_bishop_small = pygame.transform.scale(white_bishop, (34, 34))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (60, 60))
white_knight_small = pygame.transform.scale(white_knight, (34, 34))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (48, 48))
white_pawn_small = pygame.transform.scale(white_pawn, (34, 34))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# drawing board
def board():
    for i in range(32):
        column = i%4
        row = i//4
        if row%2==0:
            pygame.draw.rect(screen, 'gray90', [450 - column*150, row*75, 75, 75])
        else:
            pygame.draw.rect(screen, 'gray90', [525 - column*150, row*75, 75, 75])
        # pygame.draw.rect(screen, 'black', [0, 600, WIDTH, 75], 2)
        # pygame.draw.rect(screen, 'black', [600, 0, 150, HEIGHT], 2)
        for i in range(9):
            pygame.draw.line(screen, 'black', (75*i,0), (75*i,600))
            pygame.draw.line(screen, 'black', (0,75*i), (600,75*i))

# drawing pieces
def pieces():
    for i in range(len(white_pieces)):
        j = piece_list.index(white_pieces[i])
        if white_pieces[i]=='pawn':
            screen.blit(white_pawn, (white_locations[i][0]*75 + 16, white_locations[i][1]*75 + 22))
        else:
            screen.blit(white_images[j], (white_locations[i][0]*75 + 7, white_locations[i][1]*75 + 7))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [white_locations[i][0]*75 + 1, white_locations[i][1]*75 + 1, 74, 74], 2)
            
    for i in range(len(black_pieces)):
        j = piece_list.index(black_pieces[i])
        if black_pieces[i]=='pawn':
            screen.blit(black_pawn, (black_locations[i][0]*75 + 16, black_locations[i][1]*75 + 22))
        else:
            screen.blit(black_images[j], (black_locations[i][0]*75 + 7, black_locations[i][1]*75 + 7))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0]*75 + 1, black_locations[i][1]*75 + 1, 74, 74], 2)

# checking if castling is possible
def castling(king_location, color):
    move_list = []
    checking_list = []
    if color == 'white':
        for i in range(len(black_moves)):
            for j in range(len(black_moves[i])):
                checking_list.append(black_moves[i][j])
        if (2,0) not in checking_list and (1,0) not in checking_list and (2,0) not in white_locations and (2,0) not in black_locations and \
            (1,0) not in white_locations and (1,0) not in black_locations and king_location == (3,0) and left_castling_white == True and  \
            (3,1) not in black_locations and not check_white and ((0,1) not in black_locations or black_pieces[black_locations.index((0,1))] == 'rook'):
            move_list.append((1,0))
        if (4,0) not in checking_list and (5,0) not in checking_list and (4,0) not in white_locations and (4,0) not in black_locations and \
            (5,0) not in white_locations and (5,0) not in black_locations and (6,0) not in white_locations and (6,0) not in black_locations and king_location == (3,0) and \
            right_castling_white == True and (3,1) not in black_locations and not check_white and ((6,1) not in black_locations or black_pieces[black_locations.index((6,1))] == 'rook'):
            move_list.append((5,0))
    else:
        for i in range(len(white_moves)):
            for j in range(len(white_moves[i])):
                checking_list.append(white_moves[i][j])
        if (2,7) not in checking_list and (1,7) not in checking_list and (2,7) not in white_locations and (2,7) not in black_locations and \
            (1,7) not in white_locations and (1,7) not in black_locations and king_location == (3,7) and left_castling_black == True and  \
            (3,6) not in white_locations and not check_black and ((0,6) not in white_locations or white_pieces[white_locations.index((0,6))] == 'rook'):
            move_list.append((1,7))
        if (4,7) not in checking_list and (5,7) not in checking_list and (4,7) not in white_locations and (4,7) not in black_locations and \
            (5,7) not in white_locations and (5,7) not in black_locations and (6,7) not in black_locations and (6,7) not in white_locations and king_location == (3,7) and \
            right_castling_black == True and (3,6) not in white_locations and not check_black and ((6,6) not in white_locations or white_pieces[white_locations.index((6,6))] == 'rook'):
            move_list.append((5,7))
    return move_list

# checking if a move puts our king in check
def safe_move(potential_moves, color, piece, location):
    move_list = []
    if len(potential_moves) != 0:
        if color == 'white':
            for move in potential_moves:
                capture_check = 0
                temp = white_locations[piece]
                if move in black_locations:
                    index_move = black_locations.index(move)
                    name_piece = black_pieces[index_move]
                    black_locations.pop(index_move)
                    black_pieces.pop(index_move)
                    capture_check = 1
                white_locations[piece] = move
                if white_pieces[piece] == 'king':
                    if not checks(move, color):
                        move_list.append(move)
                else:
                    if not checks(location, color):
                        move_list.append(move)
                white_locations[piece] = temp
                if capture_check == 1:
                    black_locations.insert(index_move, move)
                    black_pieces.insert(index_move, name_piece)
        else:
            for move in potential_moves:
                capture_check = 0
                temp = black_locations[piece]
                if move in white_locations:
                    index_move = white_locations.index(move)
                    name_piece = white_pieces[index_move]
                    white_locations.pop(index_move)
                    white_pieces.pop(index_move)
                    capture_check = 1
                black_locations[piece] = move
                if black_pieces[piece] == 'king':
                    if not checks(move, color):
                        move_list.append(move)
                else:
                    if not checks(location, color):
                        move_list.append(move)
                black_locations[piece] = temp
                if capture_check == 1:
                    white_locations.insert(index_move, move)
                    white_pieces.insert(index_move, name_piece)
    return move_list

# checing valid moves for selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_moves
    else:
        options_list = black_moves
    return options_list[selection]

# drawing valid moves for selected piece
def draw_valid(moves):
    for i in range(len(moves)):
        pygame.draw.circle(screen, 'blue', (moves[i][0]*75 + 37, moves[i][1]*75 + 37), 5)

# checking valid moves
def options(pieces, locations, turn, b):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        piece = pieces[i]
        location = locations[i]
        if piece == 'pawn':
            moves_list = options_pawn(location, turn, b)
        elif piece == 'rook':
            moves_list = options_rook(location, turn, b)
        elif piece == 'knight':
            moves_list = options_knight(location, turn, b)
        elif piece == 'bishop':
            moves_list = options_bishop(location, turn, b)
        elif piece == 'queen':
            moves_list = options_queen(location, turn, b)
        elif piece == 'king':
            moves_list = options_king(location, turn, b) + castling(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# checking valid pawn moves
def options_pawn(location, color, b):
    move_list = []
    if color == 'white':
        if cross_white and location[1] == cross_location[1]-1 and \
            (location[0] == cross_location[0]+1 or location[0] == cross_location[0]-1):
            move_list.append(cross_location)
        if (location[0], location[1]+1) not in black_locations and (location[0],\
            location[1]+1) not in white_locations and location[1] < 7 :
            move_list.append((location[0], location[1]+1))
        if location[1] == 1 and (location[0], 3) not in black_locations\
            and (location[0], 3) not in white_locations and (location[0], 2) \
            not in black_locations and (location[0], 2) not in white_locations:
            move_list.append((location[0], 3))
        if (location[0]+1, location[1]+1) in black_locations :
            move_list.append((location[0]+1, location[1]+1))
        if (location[0]-1, location[1]+1) in black_locations :
            move_list.append((location[0]-1, location[1]+1))
        if b:
            move_list = safe_move(move_list, color, white_locations.index(location), white_locations[white_pieces.index('king')])
    else:
        if cross_black and location[1] == cross_location[1]+1 and \
            (location[0] == cross_location[0]+1 or location[0] == cross_location[0]-1):
            move_list.append(cross_location)
        if (location[0], location[1]-1) not in black_locations and (location[0],\
            location[1]-1) not in white_locations and location[1] > 0 :
            move_list.append((location[0], location[1]-1))
        if location[1] == 6 and (location[0], 4) not in black_locations and \
            (location[0], 4) not in white_locations and (location[0], 5) \
            not in black_locations and (location[0], 5) not in white_locations:
            move_list.append((location[0], 4))
        if (location[0]+1, location[1]-1) in white_locations :
            move_list.append((location[0]+1, location[1]-1))
        if (location[0]-1, location[1]-1) in white_locations :
            move_list.append((location[0]-1, location[1]-1))
        if b:
            move_list = safe_move(move_list, color, black_locations.index(location), black_locations[black_pieces.index('king')])
    return move_list

# checking valid rook moves
def options_rook(location, color, b):
    move_list = []
    if color == 'white':
        friends = white_locations
        enemies = black_locations
        friend_pieces = white_pieces
    else:
        friend_pieces = black_pieces
        friends = black_locations
        enemies = white_locations
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for i in range(4):
        for j in range(7):
            if (0 <= location[0]+(j+1)*directions[i][0] < 8) and (0 <= location[1]+(j+1)*directions[i][1] < 8) and \
                (location[0]+(j+1)*directions[i][0], location[1]+(j+1)*directions[i][1]) not in friends :
                move_list.append((location[0]+(j+1)*directions[i][0], location[1]+(j+1)*directions[i][1]))
            else:
                break
            if (location[0]+(j+1)*directions[i][0], location[1]+(j+1)*directions[i][1]) in enemies:
                break
    if b:
        move_list = safe_move(move_list, color, friends.index(location), friends[friend_pieces.index('king')])
    return move_list

# checking valid knight moves
def options_knight(location, color, b):
    move_list = []
    if color == 'white':
        friends = white_locations
        friend_pieces = white_pieces
    else:
        friend_pieces = black_pieces
        friends = black_locations
    directions = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
    for i in range(8):
        if 0 <= location[0]+directions[i][0] < 8 and 0 <= location[1]+directions[i][1] < 8 and \
           (location[0]+directions[i][0], location[1]+directions[i][1]) not in friends :
            move_list.append((location[0]+directions[i][0], location[1]+directions[i][1]))
    if b:
        move_list = safe_move(move_list, color, friends.index(location), friends[friend_pieces.index('king')])
    return move_list

# checking valid bishop moves
def options_bishop(location, color, b):
    move_list = []
    if color == 'white':
        friends = white_locations
        enemies = black_locations
        friend_pieces = white_pieces
    else:
        friend_pieces = black_pieces
        friends = black_locations
        enemies = white_locations
    directions = [(1,1), (1,-1), (-1,-1), (-1,1)]
    for i in range(4):
        for j in range(7):
            if (0 <= location[0]+(j+1)*directions[i][0] < 8) and (0 <= location[1]+(j+1)*directions[i][1] < 8) and \
                (location[0]+(j+1)*directions[i][0], location[1]+(j+1)*directions[i][1]) not in friends :
                move_list.append((location[0]+(j+1)*directions[i][0], location[1]+(j+1)*directions[i][1]))
            else:
                break
            if (location[0]+(j+1)*directions[i][0], location[1]+(j+1)*directions[i][1]) in enemies:
                break
        if b:
            move_list = safe_move(move_list, color, friends.index(location), friends[friend_pieces.index('king')])
    return move_list

# checking valid queen moves
def options_queen(location, color, b):
    return options_rook(location, color, b) + options_bishop(location, color, b)

# checking valid king moves
def options_king(location, color, b):
    move_list = []
    if color == 'white':
        friends = white_locations
    else:
        friends = black_locations
    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    for i in range(8):
        if (location[0]+directions[i][0], location[1]+directions[i][1]) not in friends and \
            0 <= location[0]+directions[i][0] < 8 and 0 <= location[1]+directions[i][1] < 8:
            move_list.append((location[0]+directions[i][0], location[1]+directions[i][1]))
    if b:
        move_list = safe_move(move_list, color, friends.index(location), location)
    return move_list

# drawing captured pieces
def draw_captured_pieces():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (619, 4 + 38 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (694, 4 + 38 * i))

# looking for checks
def checks(location, color):
    if color == 'white':
        enemies = options(black_pieces, black_locations, 'black', False)
    else:
        enemies = options(white_pieces, white_locations, 'white', False)
    for i in range(len(enemies)):
        if location in enemies[i]:
            return True
    return False

# game over screen
def draw_game_over(winner):
    pygame.draw.rect(screen, 'black', [200, 200, 275, 35])
    screen.blit(font.render(f'{winner} won by Checkmate', True, 'white'), (210, 210))

# stalemate screen
def draw_stalemate():
    pygame.draw.rect(screen, 'black', [200, 200, 222, 35])
    screen.blit(font.render('Draw by Stalemate!', True, 'white'), (210, 210))

black_moves = options(black_pieces, black_locations, 'black', False)
white_moves = options(white_pieces, white_locations, 'white', False)
run = True

# main game loop
while run:
    timer.tick(fps)
    screen.fill('lightblue3')
    board()
    pieces()
    draw_captured_pieces()
    
    # showing promotion options
    if promotion:
        pygame.draw.rect(screen, 'black', [200, 200, 400, 35])
        screen.blit(font.render('1:Queen   2:Rook   3:Knight   4:Bishop', True, 'white'), (210, 210))
    
    # constantly checking for rook and king moves for the sake of castling
    if (3,0) not in white_locations:
        left_castling_white = False
        right_castling_white = False
    if (0,0) not in white_locations:
        left_castling_white = False
    if (7,0) not in white_locations:
        right_castling_white = False
    if (3,7) not in black_locations:
        left_castling_black = False
        right_castling_black = False
    if (0,7) not in black_locations:
        left_castling_black = False
    if (7,7) not in black_locations:
        right_castling_black = False

    length = 0
    for i in range(len(white_pieces)):
        length += len(white_moves[i])
    if length == 0:
        if checks(white_locations[white_pieces.index('king')], 'white'):
            draw_game_over('Black')
        else:
            draw_stalemate()
    
    length = 0
    for i in range(len(black_pieces)):
        length += len(black_moves[i])
    if length == 0:
        if checks(black_locations[black_pieces.index('king')], 'black'):
            draw_game_over('White')
        else:
            draw_stalemate()
    
    # highlighting king when he's in check
    if turn_step < 2:
        if check_white:
            pygame.draw.rect(screen, 'red', [white_locations[white_pieces.index('king')][0]*75 + 1,\
                            white_locations[white_pieces.index('king')][1]*75 + 1, 74, 74], 2)
    else:
        if check_black:
            pygame.draw.rect(screen, 'red', [black_locations[black_pieces.index('king')][0]*75 + 1,\
                            black_locations[black_pieces.index('king')][1]*75 + 1, 74, 74], 2)

    if selection != 69:
        valid_moves = check_valid_moves()
        if not promotion:
            draw_valid(valid_moves)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if promotion:
            if event.type == pygame.KEYDOWN:
                if white_promotion:
                    if event.key == pygame.K_1:
                        white_pieces[white_locations.index(promotion_location)] = 'queen'
                        white_promotion = False
                        promotion = False
                        check_black = checks(black_locations[black_pieces.index('king')], 'black')  
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        turn_step = 2
                        selection = 69
                        valid_moves = []
                    if event.key == pygame.K_2:
                        white_pieces[white_locations.index(promotion_location)] = 'rook'
                        white_promotion = False
                        promotion = False
                        check_black = checks(black_locations[black_pieces.index('king')], 'black')  
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        turn_step = 2
                        selection = 69
                        valid_moves = []
                    if event.key == pygame.K_3:
                        white_pieces[white_locations.index(promotion_location)] = 'knight'
                        white_promotion = False
                        promotion = False
                        check_black = checks(black_locations[black_pieces.index('king')], 'black')  
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        turn_step = 2
                        selection = 69
                        valid_moves = []
                    if event.key == pygame.K_4:
                        white_pieces[white_locations.index(promotion_location)] = 'bishop'
                        white_promotion = False
                        promotion = False
                        check_black = checks(black_locations[black_pieces.index('king')], 'black')  
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        turn_step = 2
                        selection = 69
                        valid_moves = []
                else:
                    if event.key == pygame.K_1:
                        black_pieces[black_locations.index(promotion_location)] = 'queen'
                        promotion = False
                        check_white = checks(white_locations[white_pieces.index('king')], 'white')  
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        turn_step = 0
                        selection = 69
                        valid_moves = []
                    if event.key == pygame.K_2:
                        black_pieces[black_locations.index(promotion_location)] = 'rook'
                        promotion = False
                        check_white = checks(white_locations[white_pieces.index('king')], 'white')  
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        turn_step = 0
                        selection = 69
                        valid_moves = []
                    if event.key == pygame.K_3:
                        black_pieces[black_locations.index(promotion_location)] = 'knight'
                        promotion = False
                        check_white = checks(white_locations[white_pieces.index('king')], 'white')  
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        turn_step = 0
                        selection = 69
                        valid_moves = []
                    if event.key == pygame.K_4:
                        black_pieces[black_locations.index(promotion_location)] = 'bishop'
                        promotion = False
                        check_white = checks(white_locations[white_pieces.index('king')], 'white')  
                        black_moves = options(black_pieces, black_locations, 'black', True)
                        white_moves = options(white_pieces, white_locations, 'white', True)
                        turn_step = 0
                        selection = 69
                        valid_moves = []
           
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not promotion:
            mouse_x = event.pos[0]//75
            mouse_y = event.pos[1]//75
            mouse_cord = (mouse_x, mouse_y)
            
            cross_black = False
            cross_white = False

            # white's chance
            if turn_step < 2:
                if mouse_cord in white_locations:
                    selection = white_locations.index(mouse_cord)
                    if turn_step == 0:
                        turn_step = 1    
                if mouse_cord in valid_moves and selection != 69:
                    
                    # castling check and rook removal
                    if white_pieces[selection] == 'king':
                        if mouse_cord == (1,0):
                            white_locations[0] = (2,0)
                        if mouse_cord == (5,0):
                            white_locations[1+white_pieces[1:].index('rook')] = (4,0)
                    
                    # en passant checking
                    if white_pieces[selection] == 'pawn' and white_locations[selection][1] == 1 \
                        and mouse_cord[1] == 3:
                        cross_black = True
                        cross_location = (mouse_x, mouse_y-1)
                    
                    # en passsant execution    
                    if white_pieces[selection] == 'pawn' and mouse_cord not in black_locations and \
                        mouse_y == white_locations[selection][1]+1 and mouse_x == white_locations[selection][0]+1:
                        captured_pieces_white.append(black_pieces[black_locations.index((white_locations[selection][0]+1, white_locations[selection][1]))])
                        black_pieces.pop(black_locations.index((white_locations[selection][0]+1, white_locations[selection][1])))
                        black_locations.remove((white_locations[selection][0]+1, white_locations[selection][1]))
                    if white_pieces[selection] == 'pawn' and mouse_cord not in black_locations and \
                        mouse_y == white_locations[selection][1]+1 and mouse_x == white_locations[selection][0]-1:
                        captured_pieces_white.append(black_pieces[black_locations.index((white_locations[selection][0]-1, white_locations[selection][1]))])
                        black_pieces.pop(black_locations.index((white_locations[selection][0]-1, white_locations[selection][1])))
                        black_locations.remove((white_locations[selection][0]-1, white_locations[selection][1]))
                     
                    # changing piece location according to input   
                    white_locations[selection] = mouse_cord
                    
                    # making changes due to users move
                    if mouse_cord in black_locations:
                        black_piece = black_locations.index(mouse_cord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_locations.pop(black_piece)
                        black_pieces.pop(black_piece)
                    
                    # checking if pawn reaches last rank
                    if white_pieces[selection] == 'pawn' and mouse_y == 7:
                        promotion = True
                        promotion_location = mouse_cord
                        white_promotion = True
                        break
                    
                    # checking if my move put opponent in check
                    check_black = checks(black_locations[black_pieces.index('king')], 'black')
                    
                    # resetting variables  
                    white_moves = options(white_pieces, white_locations, 'white', True)
                    black_moves = options(black_pieces, black_locations, 'black', True)
                    turn_step = 2
                    selection = 69
                    valid_moves = []
            
            # black's chance
            if turn_step >= 2:
                if mouse_cord in black_locations:
                    selection = black_locations.index(mouse_cord)
                    if turn_step == 2:
                        turn_step = 3
                if mouse_cord in valid_moves and selection != 69:
                    
                    # castling check and rook removal
                    if black_pieces[selection] == 'king':
                        if mouse_cord == (1,7):
                            black_locations[0] = (2,7)
                        if mouse_cord == (5,7):
                            black_locations[1+black_pieces[1:].index('rook')] = (4,7)
                            
                    # en passant checking
                    if black_pieces[selection] == 'pawn' and black_locations[selection][1] == 6 \
                        and mouse_cord[1] == 4:
                        cross_white = True
                        cross_location = (mouse_x, mouse_y+1)
                    
                    # en passant execution
                    if black_pieces[selection] == 'pawn' and mouse_cord not in white_locations and \
                        mouse_y == black_locations[selection][1]-1 and mouse_x == black_locations[selection][0]+1:
                        captured_pieces_black.append(white_pieces[white_locations.index((black_locations[selection][0]+1, black_locations[selection][1]))])
                        white_pieces.pop(white_locations.index((black_locations[selection][0]+1, black_locations[selection][1])))
                        white_locations.remove((black_locations[selection][0]+1, black_locations[selection][1]))
                    if black_pieces[selection] == 'pawn' and mouse_cord not in white_locations and \
                        mouse_y == black_locations[selection][1]-1 and mouse_x == black_locations[selection][0]-1:
                        captured_pieces_black.append(white_pieces[white_locations.index((black_locations[selection][0]-1, black_locations[selection][1]))])
                        white_pieces.pop(white_locations.index((black_locations[selection][0]-1, black_locations[selection][1])))
                        white_locations.remove((black_locations[selection][0]-1, black_locations[selection][1]))
                    
                    # making changes due to users move
                    black_locations[selection] = mouse_cord
                    if mouse_cord in white_locations:
                        white_piece = white_locations.index(mouse_cord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_locations.pop(white_piece)
                        white_pieces.pop(white_piece)
                    
                    # checking if pawn reaches last rank
                    if black_pieces[selection] == 'pawn' and mouse_y == 0:
                        promotion = True
                        promotion_location = mouse_cord
                        break
                    
                    # checking if my move puts opponent in check 
                    check_white = checks(white_locations[white_pieces.index('king')], 'white')
                    
                    # resetting variables
                    black_moves = options(black_pieces, black_locations, 'black', True)
                    white_moves = options(white_pieces, white_locations, 'white', True)
                    turn_step = 0
                    selection = 69
                    valid_moves = []
                    
    pygame.display.flip()
  
pygame.quit()