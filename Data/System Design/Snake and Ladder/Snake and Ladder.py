'''
#### Name:  Snake and Ladder
Link: [link]()

'''

class Player:
    name = " "
    position = ""

class Game:

    board = [None]*101

    snakes_and_ladders = {}

    def __init__(p1, p2):
        pass

    def get_dice(): pass

    def get_next_location(dice_value): pass

    def play(players):
        # Clear board
        board[player.pos] = None

        # Get next dice value
        dice_value = get_dice()
        next_loc = get_next_location(dice_value)
        next_loc = snakes_and_ladders[next_loc]


        # Remove the another player from the board
        if (board[next_loc] == p1 and player != p1) or ():
            board[next_loc].pos = 0
            board[next_loc] = player
            palyer.pos = next_loc         