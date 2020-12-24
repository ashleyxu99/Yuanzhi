class Player2:
    """Player2 is computer AI that always chooses the 'best' move"""
    def __init__(self, board, game_controller):
        self.board = board
        self.gc = game_controller

    def move(self):
        """Choose the 'best' move"""
        # Keep track of the flip counts for all the legal moves
        flip_counts = {}
        # Loop through every single square on the board
        for i in range(len(self.board.squares.tiles)):
            for j in range(len(self.board.squares.tiles[i])):
                # Check if the current square is empty
                if not self.board.squares.tiles[i][j]:
                    # Search for flips for this empty square
                    flips = self.board.search_flips(j, i, 1)
                    # Check if there are flips for this empty square
                    if flips:
                        # Counting all the flips in all the direction
                        num_of_flips = 0
                        for direction in flips.keys():
                            num_of_flips += len(flips[direction])
                        # Keep the count in the dictionary
                        flip_counts[(i, j)] = num_of_flips

        # Check if there are legal moves
        if flip_counts:
            # Sort the flip counts for all the legal moves in ascending order
            sorted_flip_counts = sorted(
                flip_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )

            # Find the best move that has the most flip count
            best_move = sorted_flip_counts[0][0]
            self.board.put_tile(best_move[1]*100, best_move[0]*100, 1)
