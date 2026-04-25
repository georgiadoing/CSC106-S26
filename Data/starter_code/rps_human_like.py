# Created by: Kristina Striegnitz
# Last modified by: TJ Schlueter
# Complete this comment into an appropriate header comment.

import game_history
# Replace this comment by any additional import statements that you might need.

#######################################
# PREDEFINED FUNCTIONS
#######################################

# Please do not change the following function definitions.
#
# Use these functions to remember a game's result or moves until the
# next round of the game. For example, simply call
# record_computer_win() to store the information that the computer
# just won, and then call previous_result() in the next round to find
# out what the outcome of the previous round was.
def record_computer_win():
    """Record that the computer won."""
    game_history.memory.record_result(1)


def record_human_win():
    """Record that the human won."""
    game_history.memory.record_result(2)    


def record_draw():
    """Record that the game ended in a draw."""
    game_history.memory.record_result(0)


def record_computer_move(move):
    """Record a move by the computer."""
    game_history.memory.record_move("computer", move)


def record_human_move(move):
    """Record a move by the human player."""
    game_history.memory.record_move("human", move)


def previous_result():
    """Return the last recorded result. 0 indicates a draw; 1 indicates a
    computer win; and 2 indicates a human win.
    """
    return game_history.memory.get_previous_result()


def previous_computer_move():
    """Return the last recorded move by the computer."""
    return game_history.memory.get_previous_move("computer")


def previous_human_move():
    """Return the last recorded move by the human player."""
    return game_history.memory.get_previous_move("human")


def play(game):
    """
    Call the function game again and again as long as the user
    says that they want to play again.
    """
    keep_playing = 'y'
    while len(keep_playing) > 0 and keep_playing.lower()[0] == 'y':
        game()
        keep_playing = input("Do you want to play again? Type y or n.    ")
        if len(keep_playing) > 0 and keep_playing.lower()[0] == 'y':
            print("Great!")

    print("Ok. See you next time. Bye, bye!")


# Replace this comment with your definition of the function rps and any
# other function definitions you need.


### DO NOT DELETE THIS LINE: beg testing


play(rps)
