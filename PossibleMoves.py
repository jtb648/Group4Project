# Board Game Simulator
# CMPT 370 Group 4, Fall 2020
# Authors: Antoni Jann Palazo, Brian Denton, Joel Berryere,
# Michael Luciuk, Thomas Murdoch

import random

GAME_TYPE_CHESS = 0
GAME_TYPE_CHECKERS = 1


# class PossibleMoves:
#     """
#     The class defining possible moves for a piece
#     Attributes:
#         __piece: piece object wishing to move, moves to be calculated
#         __squares_you_can_move_to: List of GameSquares you can to move to
#         __game: game object to get player locations, etc
#         __board: board object, created during initialization
#     """

    # def __init__(self, game_square, game_obj):
    #     self.__game_square = game_square
    #     self.__piece = game_square.get_occupying_piece()
    #     self.__squares_you_can_move_to = []  # Will be a list of GameSquare Objects
    #     self.__game = game_obj
    #     self.__row = game_square.get_row()
    #     self.__col = game_square.get_col()
    #     self.__game_type = game_obj.get_game_type()  # will come back as either "chess" or "checkers"
    #     self.__board = self.__game.get_board()

def build_list_of_moves(game_square, game):
    """
    Determine based on the piece where it can potentially move and load it into the __squares_you_can_move_to
    attribute
    Note: Even on success, the list of possible moves for a game-square might be an empty list
    :return: 0 on success, -1 on failure
    """
    piece = game_square.get_occupying_piece()
    row = game_square.get_row()
    col = game_square.get_col()
    game_type = game.get_game_type()
    board = game.get_board()

    list_of_candidate_game_squares = []
    # 1 == checkers
    if game_type == GAME_TYPE_CHECKERS:
        # Generate possible moves for checkers

        # normal movement no capture
        # Direction Up Left
        if row > 0 and col > 0:
            if board.get_game_square(row - 1, col - 1).get_occupying_piece() is None:
                list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                   col - 1))

        # Direction Up Right
        if row > 0 and col < board.get_size() - 1:
            if board.get_game_square(row - 1, col + 1).get_occupying_piece() is None:
                list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                   col + 1))

        # capture movements
        checkers_jump(board, pieceboard.get_game_square(row, col), list_of_candidate_game_squares)


        return list_of_candidate_game_squares

    # chess = 0
    elif game_type == GAME_TYPE_CHESS:

        if type(piece).__name__ == "King":
            # A king can move one square in any direction (horizontally,
            #  vertically, or diagonally), unless the square is already occupied by a friendly piece, or the move
            #  would place the king in check

            # Moves the piece to a direction
            # check if where moving is in the board
            # check if there is a piece on that square
            # if there is check its colour
            # if not the same colour add it to the list
            # if the square was empty add it to the list

            # Direction Down
            if row < board.get_size() - 1:
                if board.get_game_square(row + 1, col).get_occupying_piece() is not None:
                    if board.get_game_square(row + 1, col).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row + 1, col))
                else:
                    list_of_candidate_game_squares.append(board.get_game_square(row + 1, col))

            # Direction Up
            if row > 0:
                if board.get_game_square(row - 1,
                                                col).get_occupying_piece() is not None:
                    if board.get_game_square(row - 1, col).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row - 1, col))
                else:
                    list_of_candidate_game_squares.append(
                        board.get_game_square(row - 1, col))

            # Direction Left
            if col > 0:
                if board.get_game_square(row,
                                                col - 1).get_occupying_piece() is not None:
                    if board.get_game_square(row, col - 1).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row, col - 1))
                else:
                    list_of_candidate_game_squares.append(
                        board.get_game_square(row, col - 1))

            # Direction Right
            if col < board.get_size() - 1:
                if board.get_game_square(row,
                                                col + 1).get_occupying_piece() is not None:
                    if board.get_game_square(row, col + 1).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row, col + 1))
                else:
                    list_of_candidate_game_squares.append(
                        board.get_game_square(row, col + 1))

            # Direction Down Left
            if row < board.get_size() - 1 and col > 0:
                if board.get_game_square(row + 1, col - 1).get_occupying_piece() is not None:
                    if board.get_game_square(row + 1, col - 1).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row + 1, col - 1))
                else:
                    list_of_candidate_game_squares.append(board.get_game_square(row + 1,
                                                                                       col - 1))

            # Direction Down Right
            if row < board.get_size() - 1 and col < board.get_size() - 1:
                if board.get_game_square(row + 1, col + 1).get_occupying_piece() is not None:
                    if board.get_game_square(row + 1, col + 1).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row + 1, col + 1))
                else:
                    list_of_candidate_game_squares.append(board.get_game_square(row + 1,
                                                                                       col + 1))

            # Direction Up Left
            if row > 0 and col > 0:
                if board.get_game_square(row - 1, col - 1).get_occupying_piece() is not None:
                    if board.get_game_square(row - 1, col - 1).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row - 1, col - 1))
                else:
                    list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                       col - 1))

            # Direction Up Right
            if row > 0 and col < board.get_size() - 1:
                if board.get_game_square(row - 1, col + 1).get_occupying_piece() is not None:
                    if board.get_game_square(row - 1, col + 1).get_occupying_piece() \
                            .get_colour() is not piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row - 1, col + 1))
                else:
                    list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                       col + 1))

            # Requirements for Castling
            # The castling must be kingside or queenside.
            # Neither the king nor the chosen rook has previously moved.
            # There are no pieces between the king and the chosen rook.
            # The king is not currently in check.
            # The king does not pass through a square that is attacked by an enemy piece.
            # The king does not end up in check. (True of any legal move.)

            # Castling
            # check if the king has not moved yet
            # check if spaces between the king and rook in a side to be empty
            # check if the rook is friendly
            # check if rook has not moved yet
            # TODO: create a function that will go over the enemy pieces and check for a checkmate
            #  so if checkmate it will not add to the list
            # add the location of the rook to be a possible move
            if not piece.get_moved_yet_status():
                # Kingside
                if board.get_game_square(7, 5).get_occupying_piece() is None and \
                        board.get_game_square(7, 6).get_occupying_piece() is None and \
                        board.get_game_square(7, 7).get_occupying_piece() is not None:
                    if type(board.get_game_square(7, 7).get_occupying_piece()).__name__ == "Rook":
                        if board.get_game_square(7, 7).get_occupying_piece() \
                                .get_colour() is piece.get_colour():
                            if not board.get_game_square(7, 7).get_occupying_piece().get_moved_yet_status():
                                list_of_candidate_game_squares.append(board.get_game_square(7, 7))

                # Queenside
                if board.get_game_square(7, 3).get_occupying_piece() is None and \
                        board.get_game_square(7, 2).get_occupying_piece() is None and \
                        board.get_game_square(7, 1).get_occupying_piece() is None and \
                        board.get_game_square(7, 0).get_occupying_piece() is not None:
                    if type(board.get_game_square(7, 0).get_occupying_piece()).__name__ == "Rook":
                        if board.get_game_square(7, 0).get_occupying_piece() \
                                .get_colour() is piece.get_colour():
                            if not board.get_game_square(7, 0).get_occupying_piece().get_moved_yet_status():
                                list_of_candidate_game_squares.append(board.get_game_square(7, 0))



        elif type(piece).__name__ == "Queen":
            # The queen can be moved any number of unoccupied squares in a straight line
            # vertically, horizontally, or diagonally, thus combining the moves of the rook and bishop
            # Vertical movements
            # check from the piece to a direction: up, down, left, right
            # will stop until sees a peace
            # if piece friendly stop
            # if non friendly add add (row, col) to possible moves but also stops
            # if empty then add it to list and keep going

            # Vertical movements

            # Vertical UP
            # check from piece to top row -- (row, col) -> (0, col)
            row_pos = row
            while row_pos != 0:
                row_pos -= 1
                if board.get_game_board()[row_pos][col].get_occupying_piece() is not None:
                    if board.get_game_board()[row_pos][col].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row_pos][col].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(board.get_game_board()[row_pos][col])
                        break
                else:
                    list_of_candidate_game_squares.append(board.get_game_board()[row_pos][col])

            # Vertical DOWN
            # check from piece to bot row -- (row, col) -> (7, col)
            row_neg = row
            while row_neg != board.get_size() - 1:
                row_neg += 1
                if board.get_game_board()[row_neg][col].get_occupying_piece() is not None:
                    if board.get_game_board()[row_neg][col].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row_neg][col].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(board.get_game_board()[row_neg][col])
                        break
                else:
                    list_of_candidate_game_squares.append(board.get_game_board()[row_neg][col])

            # Horizontal movements

            # Horizontal RIGHT
            # check from piece to right col -- (row, col) -> (row, 7)
            col_pos = col
            while col_pos != board.get_size() - 1:
                col_pos += 1
                if board.get_game_board()[row][col_pos].get_occupying_piece() is not None:

                    if board.get_game_board()[row][col_pos].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row][col_pos].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(board.get_game_board()[row][col_pos])
                        break
                else:
                    list_of_candidate_game_squares.append(board.get_game_board()[row][col_pos])

            # Horizontal LEFT
            # check from piece to left col -- (row, col) -> (row, 0)
            col_neg = col
            while col_neg != 0:
                col_neg -= 1
                if board.get_game_board()[row][col_neg].get_occupying_piece() is not None:
                    if board.get_game_board()[row][
                        col_neg].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row][
                        col_neg].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_board()[row][col_neg])
                        break
                else:
                    list_of_candidate_game_squares.append(
                        board.get_game_board()[row][col_neg])

            # check if the row or column are out of bounds
            # check specific corner from piece
            # will stop until sees a peace
            # if piece friendly stop
            # if non friendly add add (row, col) to possible moves but also stops
            # if empty then add it to list and keep going

            # Top Right
            row_pos = row
            col_pos = col

            stopper = False
            if row_pos != 0:
                for row in range(row_pos - 1, -1, -1):
                    if col_pos != board.get_size() - 1:
                        if not stopper:
                            for col in range(col_pos + 1, board.get_size()):
                                if abs(row_pos - row) == abs(col_pos - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break


            # Top Left
            row_pos = row
            col_neg = col

            stopper = False
            if row_pos != 0:
                for row in range(row_pos - 1, -1, -1):
                    if col_neg != 0:
                        if not stopper:
                            for col in range(col_neg - 1, -1, -1):
                                if abs(row_pos - row) == abs(col_neg - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break


            # Bottom Right
            row_neg = row
            col_pos = col

            stopper = False
            if row_neg != board.get_size() - 1:
                for row in range(row_neg + 1, board.get_size()):
                    if col_pos != board.get_size() - 1:
                        if not stopper:
                            for col in range(col_pos + 1, board.get_size()):
                                if abs(row_neg - row) == abs(col_pos - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break

            # Bottom Left
            row_neg = row
            col_neg = col

            stopper = False
            if row_neg != board.get_size():
                for row in range(row_neg + 1, board.get_size()):
                    if col_neg != 0:
                        if not stopper:
                            for col in range(col_neg - 1, -1, -1):
                                if abs(row_neg - row) == abs(col_neg - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break



        elif type(piece).__name__ == "Bishop":
            # The bishop can be moved any number of unoccupied squares in a straight line diagonally

            # check if the row or column are out of bounds
            # check specific corner from piece
            # will stop until sees a peace
            # if piece friendly stop
            # if non friendly add add (row, col) to possible moves but also stops
            # if empty then add it to list and keep going

            # Top Right
            row_pos = row
            col_pos = col

            stopper = False
            if row_pos != 0:
                for row in range(row_pos - 1, -1, -1):
                    if col_pos != board.get_size() - 1:
                        if not stopper:
                            for col in range(col_pos + 1, board.get_size()):
                                if abs(row_pos - row) == abs(col_pos - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break



            # Top Left
            row_pos = row
            col_neg = col

            stopper = False
            if row_pos != 0:
                for row in range(row_pos - 1, -1, -1):
                    if col_neg != 0:
                        if not stopper:
                            for col in range(col_neg - 1, -1, -1):
                                if abs(row_pos - row) == abs(col_neg - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break


            # Bottom Right
            row_neg = row
            col_pos = col

            stopper = False
            if row_neg != board.get_size() - 1:
                for row in range(row_neg + 1, board.get_size()):
                    if col_pos != board.get_size() - 1:
                        if not stopper:
                            for col in range(col_pos + 1, board.get_size()):
                                if abs(row_neg - row) == abs(col_pos - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break

            # Bottom Left
            row_neg = row
            col_neg = col

            stopper = False
            if row_neg != board.get_size():
                for row in range(row_neg + 1, board.get_size()):
                    if col_neg != 0:
                        if not stopper:
                            for col in range(col_neg - 1, -1, -1):
                                if abs(row_neg - row) == abs(col_neg - col):
                                    if board.get_game_board()[row][col].get_occupying_piece() is not None:
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() == piece.get_colour():
                                            stopper = True
                                            break
                                        if board.get_game_board()[row][col].get_occupying_piece() \
                                                .get_colour() != piece.get_colour():
                                            list_of_candidate_game_squares.append(
                                                board.get_game_board()[row][col])
                                            stopper = True
                                            break
                                    else:
                                        list_of_candidate_game_squares.append(
                                            board.get_game_board()[row][col])
                        else:
                            break



        elif type(piece).__name__ == "Knight":

            # check if the possible move (row, col) is in the board or check for bounds
            # check if game square has a piece
            # check if it has a non friendly piece if so add to list of moves
            # if game sqaure is empty add it to list of moves

            # moves up then right
            if ((row - 2) >= 0) and ((col + 1) <= board.get_size() - 1):
                if board.get_game_square(row - 2, col + 1).get_occupying_piece() is not None:
                    if (board.get_game_square(row - 2, col + 1).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        up_right_square = board.get_game_square(row - 2, col + 1)
                        list_of_candidate_game_squares.append(up_right_square)
                elif board.get_game_square(row - 2, col + 1).get_occupying_piece() is None:
                    up_right_square = board.get_game_square(row - 2, col + 1)
                    list_of_candidate_game_squares.append(up_right_square)

            # moves up then left
            if ((row - 2) >= 0) and ((col - 1) >= 0):
                if board.get_game_square(row - 2, col - 1).get_occupying_piece() is not None:
                    if (board.get_game_square(row - 2, col - 1).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        up_left_square = board.get_game_square(row - 2, col - 1)
                        list_of_candidate_game_squares.append(up_left_square)
                elif board.get_game_square(row - 2, col - 1).get_occupying_piece() is None:
                    up_left_square = board.get_game_square(row - 2, col - 1)
                    list_of_candidate_game_squares.append(up_left_square)

            # moves down then right
            if ((row + 2) <= board.get_size() - 1) \
                    and ((col + 1) <= board.get_size() - 1):
                if board.get_game_square(row + 2, col + 1).get_occupying_piece() is not None:
                    if (board.get_game_square(row + 2, col + 1).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        down_right_square = board.get_game_square(row + 2, col + 1)
                        list_of_candidate_game_squares.append(down_right_square)
                elif board.get_game_square(row + 2, col + 1).get_occupying_piece() is None:
                    down_right_square = board.get_game_square(row + 2, col + 1)
                    list_of_candidate_game_squares.append(down_right_square)

            # moves down then left
            if ((row + 2) <= board.get_size() - 1) and ((col - 1) >= 0):
                if board.get_game_square(row + 2, col - 1).get_occupying_piece() is not None:
                    if (board.get_game_square(row + 2, col - 1).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        down_left_square = board.get_game_square(row + 2, col - 1)
                        list_of_candidate_game_squares.append(down_left_square)
                elif board.get_game_square(row + 2, col - 1).get_occupying_piece() is None:
                    down_left_square = board.get_game_square(row + 2, col - 1)
                    list_of_candidate_game_squares.append(down_left_square)

            # moves right then up
            if ((row - 1) >= 0) and ((col + 2) <= board.get_size() - 1):
                if board.get_game_square(row - 1, col + 2).get_occupying_piece() is not None:
                    if (board.get_game_square(row - 1, col + 2).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        right_up_square = board.get_game_square(row - 1, col + 2)
                        list_of_candidate_game_squares.append(right_up_square)
                elif board.get_game_square(row - 1, col + 2).get_occupying_piece() is None:
                    right_up_square = board.get_game_square(row - 1, col + 2)
                    list_of_candidate_game_squares.append(right_up_square)

            # moves right then down
            if ((row + 1) <= board.get_size() - 1) \
                    and ((col + 2) <= board.get_size() - 1):
                if board.get_game_square(row + 1, col + 2).get_occupying_piece() is not None:
                    if (board.get_game_square(row + 1, col + 2).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        right_down_square = board.get_game_square(row + 1, col + 2)
                        list_of_candidate_game_squares.append(right_down_square)
                elif board.get_game_square(row + 1, col + 2).get_occupying_piece() is None:
                    right_down_square = board.get_game_square(row + 1, col + 2)
                    list_of_candidate_game_squares.append(right_down_square)

            # moves left then up
            if ((row - 1) >= 0) and ((col - 2) >= 0):
                if board.get_game_square(row - 1, col - 2).get_occupying_piece() is not None:
                    if (board.get_game_square(row - 1, col - 2).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        left_up_square = board.get_game_square(row - 1, col - 2)
                        list_of_candidate_game_squares.append(left_up_square)
                elif board.get_game_square(row - 1, col - 2).get_occupying_piece() is None:
                    left_up_square = board.get_game_square(row - 1, col - 2)
                    list_of_candidate_game_squares.append(left_up_square)

            # moves left then down
            if ((row + 1) <= board.get_size() - 1) and ((col - 2) >= 0):
                if board.get_game_square(row + 1, col - 2).get_occupying_piece() is not None:
                    if (board.get_game_square(row + 1, col - 2).get_occupying_piece()
                            .get_colour() is not piece.get_colour()):
                        # need to find out how to capture a piece
                        left_down_square = board.get_game_square(row + 1, col - 2)
                        list_of_candidate_game_squares.append(left_down_square)
                elif board.get_game_square(row + 1, col - 2).get_occupying_piece() is None:
                    left_down_square = board.get_game_square(row + 1, col - 2)
                    list_of_candidate_game_squares.append(left_down_square)

        elif type(piece).__name__ == "Rook":
            # The rook can be moved any number of unoccupied squares in a straight line vertically or horizontally

            # check from the piece to a direction: up, down, left, right
            # will stop until sees a peace
            # if piece friendly stop
            # if non friendly add add (row, col) to possible moves but also stops
            # if empty then add it to list and keep going

            # Vertical movements

            # Vertical UP
            # check from piece to top row -- (row, col) -> (0, col)
            row_pos = row
            while row_pos != 0:
                row_pos -= 1
                if board.get_game_board()[row_pos][col].get_occupying_piece() is not None:
                    if board.get_game_board()[row_pos][col].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row_pos][col].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(board.get_game_board()[row_pos][col])
                        break
                else:
                    list_of_candidate_game_squares.append(board.get_game_board()[row_pos][col])

            # Vertical DOWN
            # check from piece to bot row -- (row, col) -> (7, col)
            row_neg = row
            while row_neg != board.get_size() - 1:
                row_neg += 1
                if board.get_game_board()[row_neg][col].get_occupying_piece() is not None:
                    if board.get_game_board()[row_neg][col].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row_neg][col].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(board.get_game_board()[row_neg][col])
                        break
                else:
                    list_of_candidate_game_squares.append(board.get_game_board()[row_neg][col])

            # Horizontal movements

            # Horizontal RIGHT
            # check from piece to right col -- (row, col) -> (row, 7)
            col_pos = col
            while col_pos != board.get_size() - 1:
                col_pos += 1
                if board.get_game_board()[row][col_pos].get_occupying_piece() is not None:

                    if board.get_game_board()[row][col_pos].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row][col_pos].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(board.get_game_board()[row][col_pos])
                        break
                else:
                    list_of_candidate_game_squares.append(board.get_game_board()[row][col_pos])

            # Horizontal LEFT
            # check from piece to left col -- (row, col) -> (row, 0)
            col_neg = col
            while col_neg != 0:
                col_neg -= 1
                if board.get_game_board()[row][col_neg].get_occupying_piece() is not None:
                    if board.get_game_board()[row][
                        col_neg].get_occupying_piece().get_colour() == \
                            piece.get_colour():
                        break
                    if board.get_game_board()[row][
                        col_neg].get_occupying_piece().get_colour() != \
                            piece.get_colour():
                        list_of_candidate_game_squares.append(
                            board.get_game_board()[row][col_neg])
                        break
                else:
                    list_of_candidate_game_squares.append(
                        board.get_game_board()[row][col_neg])


        elif type(piece).__name__ == "Pawn":
            # Normally a pawn moves by advancing a single square,
            #  but the first time a pawn moves, it has the option of advancing two squares. Pawns may not use the
            #  initial two-square advance to jump over an occupied square, or to capture. Any piece immediately 
            #  in front of a pawn, friend or foe, blocks its advance.

            # Normal movements
            # forward 1 step and 2 step
            if row > 0:
                # 1 step
                if board.get_game_square(row - 1, col).get_occupying_piece() is None:
                    list_of_candidate_game_squares.append(board.get_game_square(row - 1, col))

                # 2 step
                if not piece.get_moved_yet_status():
                    if board.get_game_square(row - 2, col).get_occupying_piece() is None:
                        list_of_candidate_game_squares.append(
                            board.get_game_square(row - 2, col))

            # diagonal movements
            # only used when non friendly piece on the front diagonal sides
            # check if inside the board
            # check for edge case for columns 0 and 7
            # if they are just check one diagonal side
            # check if there is a non friendly
            # then add it
            if row > 0 and 0 <= col <= board.get_size() - 1:

                # left most case
                if col == 0:
                    if board.get_game_square(row - 1,
                                                    col + 1).get_occupying_piece() is not None:
                        if board.get_game_square(row - 1, col + 1).get_occupying_piece() \
                                .get_colour() is not piece.get_colour():
                            list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                               col + 1))

                # right most case:
                elif col == board.get_size() - 1:
                    if board.get_game_square(row - 1,
                                                    col - 1).get_occupying_piece() is not None:
                        if board.get_game_square(row - 1, col - 1).get_occupying_piece() \
                                .get_colour() is not piece.get_colour():
                            list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                               col - 1))

                # Non edge case
                # checks for both sides of the diagonal front
                # if there is a non friendly add it to the list
                else:
                    # front left
                    if board.get_game_square(row - 1,
                                                    col - 1).get_occupying_piece() is not None:
                        if board.get_game_square(row - 1, col - 1).get_occupying_piece() \
                                .get_colour() is not piece.get_colour():
                            list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                               col - 1))
                    # front right
                    if board.get_game_square(row - 1,
                                                    col - 1).get_occupying_piece() is not None:
                        if board.get_game_square(row - 1, col - 1).get_occupying_piece() \
                                .get_colour() is not piece.get_colour():
                            list_of_candidate_game_squares.append(board.get_game_square(row - 1,
                                                                                               col - 1))


        else:
            # Could not identify the type of piece
            return -1

        return list_of_candidate_game_squares

    else:
        # Game mode is neither "chess" nor "checkers"
        return game_type.lower()

# def select_best(self, candidate_game_squares):
#     """
#     Chooses and return the best game square to move to from a list of candidate squares
#     :param: List of GameSquares to choose from
#     :return: GameSquare, the best game square to move to. Returns None if there are no moves for that square
#     """
#     if not candidate_game_squares:
#         # List of moves is empty
#         return None
#     elif len(candidate_game_squares) == 1:
#         # The is only one move, it has to be the best
#         return candidate_game_squares[0]
#     else:
#         # TODO: Some AI code to evaluate the list of moves to choose the best one, in the mean time we are jsut
#         #  returning the first one in the list
#         # Right now we will just return a random one
#         random_index = (random.randrange(0, len(candidate_game_squares), 1))
#         return candidate_game_squares[random_index]

# def get_list_of_squares_you_can_move_to(self):
#     """
#     :return: GameSquare[]: A list of game squares that are legal to move to
#     """
#     return self.__squares_you_can_move_to

# Added functions might not be in the domain model yet
# ------------------------------------------------------------------------------------------------
def checkers_jump(board, piece, gamesquare, list_moves):
    # Direction Up Left

    # checks if top left is on the board
    if gamesquare.get_row() - 1 > 0 and gamesquare.get_col() - 1 > 0:
        # check if there is a coin there
        if board.get_game_square(gamesquare.get_row() - 1,
                                        gamesquare.get_col() - 1).get_occupying_piece() is not None:
            # check if its an enemy piece
            if board.get_game_square(gamesquare.get_row() - 1,
                                            gamesquare.get_col() - 1).get_occupying_piece().get_colour() is not \
                    piece.get_colour():
                # check if up left of the enemy coin is on the board
                if gamesquare.get_row() >= 0 and gamesquare.get_col() - 2 >= 0:
                    # check if up left of the enemy coin is empty
                    if board.get_game_square(gamesquare.get_row() - 2,
                                                    gamesquare.get_col() - 2).get_occupying_piece() is None:
                        # can move there
                        list_moves.append(
                            board.get_game_square(gamesquare.get_row() - 2, gamesquare.get_col() - 2))
                        # check if coin can jump more
                        checkers_jump(board, piece, board.get_game_square(gamesquare.get_row() - 2,
                                                                        gamesquare.get_col() - 2), list_moves)

                        # look for another enemy to capture

    # checks if top right is on the board
    if gamesquare.get_row() - 1 > 0 and gamesquare.get_col() + 1 < board.get_size() - 1:
        # check if there is a coin there
        if board.get_game_square(gamesquare.get_row() - 1,
                                        gamesquare.get_col() + 1).get_occupying_piece() is not None:
            # check if its an enemy piece
            if board.get_game_square(gamesquare.get_row() - 1,
                                            gamesquare.get_col() + 1).get_occupying_piece().get_colour() is not \
                    piece.get_colour():
                # check if up left of the enemy coin is on the board
                if gamesquare.get_row() >= 0 and gamesquare.get_col() + 2 <= board.get_size() - 1:
                    # check if up left of the enemy coin is empty
                    if board.get_game_square(gamesquare.get_row() - 2,
                                                    gamesquare.get_col() + 2).get_occupying_piece() is None:
                        # can move there
                        list_moves.append(
                            board.get_game_square(gamesquare.get_row() - 2, gamesquare.get_col() + 2))
                        # check if coin can jump more
                        checkers_jump(board, piece, board.get_game_square(gamesquare.get_row() - 2,
                                                                        gamesquare.get_col() + 2), list_moves)

# ------------------------------------------------------------------------------------------------
