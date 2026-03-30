class AI:

    def evaluate(self,board):

        score = 0

        for row in board.board:
            for piece in row:

                if piece:
                    if piece.color == "black":
                        score += 1
                    else:
                        score -= 1

        return score

    def minimax(self,board,depth,maximizing,alpha,beta):

        if depth == 0:
            return self.evaluate(board)

        if maximizing:

            max_eval = -999

            for move in board.get_all_moves("black"):

                new_board = board.clone()
                new_board.move(move[0],move[1])

                eval = self.minimax(new_board,depth-1,False,alpha,beta)

                max_eval = max(max_eval,eval)
                alpha = max(alpha,eval)

                if beta <= alpha:
                    break

            return max_eval

        else:

            min_eval = 999

            for move in board.get_all_moves("white"):

                new_board = board.clone()
                new_board.move(move[0],move[1])

                eval = self.minimax(new_board,depth-1,True,alpha,beta)

                min_eval = min(min_eval,eval)
                beta = min(beta,eval)

                if beta <= alpha:
                    break

            return min_eval

    def get_best_move(self,board):

        best_score = -999
        best_move = None

        for move in board.get_all_moves("black"):

            new_board = board.clone()
            new_board.move(move[0],move[1])

            score = self.minimax(new_board,2,False,-999,999)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move