def babuji(n):
    if n == 0:
        print()
    elif n > 0:
        print("nimbu paani")  # ,n)
        babuji(n - 1)
        print("paani nimbu")  # ,n)


# # DRIVER CODE # #
babuji(3)
