# Created by: Kristina Striegnitz
# Last modified by: TJ Schlueter
# Complete this comment into an appropriate header comment.

# Replace this comment by copying and pasting your import statements and
# function definitions from rps_1.py

#######################################
# PREDEFINED FUNCTION
#######################################

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


### DO NOT DELETE THIS LINE: beg testing

# Calling the function play like this should play rock-paper-scissors
# and then ask the user whether they want to play again. The computer
# will repeat to do this until the user eventually answers 'n' to
# indicate that they don't want to play anymore.
play(rps)
