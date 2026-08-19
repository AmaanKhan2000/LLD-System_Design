from typing import List
class ChessPiece:
    def __init__(self, piece:str, color:str, position:str):
        self.piece = piece
        self.color = color
        self.position = position
    def display(self):
        return f"{self.color} {self.piece} is at position {self.position}"    

class ChessBoard:
    def __init__(self):
        self.pieces: List[ChessPiece] = []
    def add_piece(self, piece: ChessPiece):
        self.pieces.append(piece)
    def display_board(self):
        for p in self.pieces:
            print(f"{p.display()}")

piece1 = ChessPiece("King", "Black", "e4")
piece2 = ChessPiece("Queen", "Black", "e5")
piece3 = ChessPiece("Horse", "Black", "e7")
piece4 = ChessPiece("Knight", "Black", "e6")
piece5 = ChessPiece("King", "White", "s2")

chess_board = ChessBoard()
chess_board.add_piece(piece1)
chess_board.add_piece(piece2)
chess_board.add_piece(piece3)
chess_board.add_piece(piece4)
chess_board.add_piece(piece5)

chess_board.display_board()

new_chess_board = ChessBoard()
for p in chess_board.pieces:
    new_chess_board.pieces.append(p)
print("--------- ")
new_chess_board.display_board()

