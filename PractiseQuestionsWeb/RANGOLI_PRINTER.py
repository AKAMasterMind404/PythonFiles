def print_rangoli(n):
    rows = 2 * n - 1  # n-1 + 1(central element) + n-1
    columns = 4 * n - 3
    column_mid = (n - 1) * 2
    row_mid = n - 1

    for row in range(rows):
        for column in range(columns):
            toPrint = n - row
            if row > row_mid:
                toPrint = abs(toPrint) + 2

            revised_row = row
            if row > row_mid:
                revised_row = 2 * row_mid - row

            start_at = column_mid - (revised_row) * 2
            end_at = column_mid + (revised_row) * 2

            if column in range(start_at, end_at + 1):
                if row == row_mid and column == 0 or not column % 2:
                    if column == column_mid:
                        print(chr(toPrint + 96), end='')
                    else:
                        here = int(toPrint + (column_mid - column) / 2)
                        if column > column_mid:
                            here = int(toPrint + (column - column_mid) / 2)
                        print(chr(here + 96), end='')
                elif column % 2:
                    print('-', end='')
            else:
                print('-', end='')
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
