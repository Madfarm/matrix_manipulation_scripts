import pygame
import sys

pygame.init()

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (242, 85, 96)
CROSS_COLOR = (85, 170, 255)

# Screen
WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Setting up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(WHITE)

# Board
board = [['' for x in range(BOARD_COLS)] for y in range(BOARD_ROWS)]

# Drawing functions
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Checking for a win
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win('O'):
        return -10
    if check_win('X'):
        return 10
    if len(available_moves(board)) == 0:
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ''
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ''
            min_eval = min(min_eval, eval)
        return min_eval

def best_move():
    max_eval = float('-inf')
    move = (0, 0)

    for cell in available_moves(board):
        board[cell[0]][cell[1]] = 'X'
        eval = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ''
        if eval > max_eval:
            max_eval = eval
            move = cell

    return move

def available_moves(board):
    moves = []
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == '':
                moves.append((i, j))
    return moves

def reset():
    screen.fill(WHITE)
    draw_lines()
    player = 'O'
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''

draw_lines()

player = 'O'
game_over = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over:
            continue

        if player == 'O':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                if board[clicked_row][clicked_col] == '':
                    board[clicked_row][clicked_col] = 'O'
                    if check_win(player):
                        game_over = True
                    player = 'X'

        elif player == 'X':
            row, col = best_move()
            if board[row][col] == '':
                board[row][col] = 'X'
                if check_win(player):
                    game_over = True
                player = 'O'

        draw_figures()

    pygame.display.update()