class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[0][0] = 'N'

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def move_knight(self, moves):
        x, y = 0, 0
        for move in moves:
            dx, dy = 0, 0
            if move == 'up':
                dx, dy = -2, -1
            elif move == 'down':
                dx, dy = 2, 1
            elif move == 'left':
                dx, dy = -1, -2
            elif move == 'right':
                dx, dy = 1, 2
            elif move == 'up_left':
                dx, dy = -1, -2
            elif move == 'up_right':
                dx, dy = 1, -2
            elif move == 'down_left':
                dx, dy = -1, 2
            elif move == 'down_right':
                dx, dy = 1, 2
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y):
                self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
                x, y = new_x, new_y
        self.display_board()


def main():
    chess_board = ChessBoard()
    chess_board.display_board()
    moves = ['up_right', 'down_right', 'down_left', 'up_left']
    chess_board.move_knight(moves)


if __name__ == "__main__":
    main()