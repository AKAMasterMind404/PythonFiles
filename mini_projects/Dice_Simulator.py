import random

'''
   # # # # # #
  #         ##
 #         # #
# # # # # #  #
#         #  #
#  # # #  #  #
#  # # #  #  #
#         # #
# # # # # #

'''


def getNumberedDice(num):
    dice = ''
    top = "   # # # # # #\n" \
          "  #         ##\n" \
          " #         # #\n" \
          "# # # # # #  #\n"

    bottom = "\n" \
             "#         # #\n" \
             "# # # # # #"
    if num == 1:
        dice = "#         #  #\n" \
               "#    #    #  #\n" \
               "#         #  #"
    if num == 2:
        dice = "#         #  #\n" \
               "#    #    #  #\n" \
               "#    #    #  #"
    if num == 3:
        dice = "#         #  #\n" \
               "#    #    #  #\n" \
               "#   # #   #  #"
    if num == 4:
        dice = "#         #  #\n" \
               "#   # #   #  #\n" \
               "#   # #   #  #"
    if num == 5:
        dice = "#   # #   #  #\n" \
               "#    #    #  #\n" \
               "#   # #   #  #"
    if num == 6:
        dice = "#         #  #\n" \
               "#  # # #  #  #\n" \
               "#  # # #  #  #"
    return top + dice + bottom


if __name__ == '__main__':
    r = 0
    for i in range(10):
        r = random.randint(1, 6)
    print(getNumberedDice(r))
# 1 :
#         #  #
#    #    #  #
#         #  #

# 2 :
#         #  #
#    #    #  #
#    #    #  #

# 3 :
#         #  #
#    #    #  #
#   # #   #  #

# 4 :
#         #  #
#   # #   #  #
#   # #   #  #

# 5 :
#   # #   #  #
#    #    #  #
#   # #   #  #

# 6 :
#         #  #
#  # # #  #  #
#  # # #  #  #
