class ChessBoard:
    def __init__(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        self.board[0][0] = 'N'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, moves):
        for move in moves:
            from_row, from_col = self.find_piece()
            to_row, to_col = self.parse_move(move)
            self.board[to_row][to_col] = self.board[from_row][from_col]
            self.board[from_row][from_col] = '.'
        self.print_board()

    def find_piece(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != '.':
                    return i, j

    def parse_move(self, move):
        return ord(move[0]) - ord('a'), int(move[1]) - 1


def main():
    board = ChessBoard()
    board.print_board()

    moves = ['b3', 'c5', 'd7', 'e8', 'f6', 'g4', 'h2', 'a1']
    board.move_piece(moves)


if __name__ == "__main__":
    main()