from typing import List
import copy
class ChessPiece:
    def __init__(self, piece:str, color:str, position:str):
        self.piece = piece
        self.color = color
        self.position = position
    def display(self):
        return f"{self.color} {self.piece} is at position {self.position}"    
    def clone(self):
        return copy.deepcopy(self)

class ChessBoard:
    def __init__(self):
        self.pieces: List[ChessPiece] = []
    def add_piece(self, piece: ChessPiece):
        self.pieces.append(piece)
    def display_board(self):
        for p in self.pieces:
            print(f"{p.display()}")
    def clone(self):
        return copy.deepcopy(self)


piece1 = ChessPiece("King", "Black", "e4")
piece2 = ChessPiece("Queen", "Black", "e5")
piece3 = ChessPiece("Horse", "Black", "e7")
piece4 = ChessPiece("Knight", "Black", "e6")
piece5 = ChessPiece("King", "White", "s2")
piece6 = ChessPiece.clone(piece4)

chess_board = ChessBoard()
chess_board.add_piece(piece1)
chess_board.add_piece(piece2)
chess_board.add_piece(piece3)
chess_board.add_piece(piece4)
chess_board.add_piece(piece5)
chess_board.add_piece(piece6)

chess_board.display_board()

print("--------------------")

new_chess_board = ChessBoard.clone(chess_board)

piece10 = ChessPiece("King","King", "King")

new_chess_board.add_piece(piece10)
new_chess_board.display_board()
