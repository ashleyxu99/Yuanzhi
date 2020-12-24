class GameController:
    """Maintain the state of the game"""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        # Let the human (player1) go first
        self.player1_turn = True
        self.game_over = False
        self.player1_score = 2
        self.player2_score = 2
        self.delay_counter = 100
        self.is_saved = False
        self.delay_counter2 = 120

    def display_welcome_message(self):
        """
        Display message at start of game welcoming player and introducing rules
        """
        print("Welcome to Yuanzhi's Othello Game!")
        print("You are playing the black tiles. Click a location on the " +
              "gameboard to make your first move.\n")

    def update(self):
        """Carry out necessary updates per-frame"""
        # If the game is not over
        if not self.game_over:
            # If it's human's (player1's) turn
            if self.player1_turn:
                # Create delay before showing the announcement
                if 50 < self.delay_counter <= 100:
                    # Count down the delay counter
                    self.delay_counter -= 1
                # Create delay for showing the announcement
                elif 0 < self.delay_counter <= 50:
                    # Announce it's human's (player1's) turn
                    fill(0.7, 0.5, 0.2)
                    textSize(50)
                    text("It's your turn", self.WIDTH/2 - 150, self.HEIGHT/2)
                    # Count down the delay counter
                    self.delay_counter -= 1

        # If the game is not over
        if not self.game_over:
            # If it's computer's (player2's) turn
            if not self.player1_turn:
                # Create delay before showing the announcement
                if 50 < self.delay_counter <= 100:
                    # Count down the delay counter
                    self.delay_counter -= 1
                # Create delay for showing the announcement
                elif 0 < self.delay_counter <= 50:
                    # Announcing it's computer's (player2's) turn
                    fill(0.7, 0.5, 0.2)
                    textSize(50)
                    text("It's computer's turn",
                         self.WIDTH/2 - 230,
                         self.HEIGHT/2)
                    # Count down the delay counter
                    self.delay_counter -= 1

        # If the game is over
        if self.game_over:
            fill(0.7, 0.5, 0.2)
            textSize(50)
            if self.player1_score == self.player2_score:
                text("PLAYERS TIE", self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.player1_score > self.player2_score:
                text("YOU WIN!", self.WIDTH/2 - 140, self.HEIGHT/2)
            else:
                text("COMPUTER WIN!", self.WIDTH/2 - 140, self.HEIGHT/2)
            text("YOU: " + str(self.player1_score),
                 self.WIDTH/2 - 140, self.HEIGHT/2 + 60)
            text("COMPUTER: " + str(self.player2_score),
                 self.WIDTH/2 - 140, self.HEIGHT/2 + 120)

            self.delay_counter2 -= 1
            if self.delay_counter2 == 0 and not self.is_saved:
                user_name = self.input("Enter your name:")
                if user_name:
                    try:
                        f_to_r = open("scores.txt", "r")
                    except FileNotFoundError:
                        print("Can't find scores.txt")

                    highest = True
                    lines = []
                    user_score = self.player1_score
                    for line in f_to_r:
                        lines.append(line)
                        the_score = int(line.strip().split(" ")[1])
                        if the_score >= user_score:
                            highest = False

                    f_to_r.close()

                    if highest:
                        lines.insert(0, user_name+" "+ str(user_score)+"\n")
                    else:
                        lines.append(user_name+" "+ str(user_score)+"\n")

                    try:
                        f_to_w = open("scores.txt", "w")
                    except FileNotFoundError:
                        print("Can't find scores.txt")

                    for line in lines:
                        f_to_w.write(line)

                    f_to_w.close()
                    self.is_saved = True

                elif user_name == '':
                    print('[empty string]')
                else:
                    print(user_name)  # Canceled dialog will print None

                self.delay_counter2 = 120

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
