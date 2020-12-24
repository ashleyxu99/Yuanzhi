from game_controller import GameController
from board import Board
from player1 import Player1
from player2 import Player2

WIDTH = 800
HEIGHT = 800
time_delay_counter = 120

game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, game_controller)
player1 = Player1(board, game_controller)
player2 = Player2(board, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    global time_delay_counter
    background(0, 0.35, 0)
    # Display the board
    board.display()
    # Update the game controller
    game_controller.update()
    # If the game is not over
    if not game_controller.game_over:
        # If it's the computer's (player2's) turn
        if not game_controller.player1_turn:
            # Count down the delay counter
            time_delay_counter -= 1
            # If the delay counter counts down to zero
            if time_delay_counter == 0:
                # The computer (player2) make a move
                player2.move()
                # Reset the delay counter
                time_delay_counter = 120


def mousePressed():
    # If the game is not over
    if not game_controller.game_over:
        # If it's the human's (player1's) turn
        if game_controller.player1_turn:
            # The human (player1) make a move
            player1.move(mouseX, mouseY)
