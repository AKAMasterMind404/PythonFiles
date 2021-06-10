def zero(*operation: tuple) -> int:  # your code here
    if not len(operation): return 0
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 0 + operand
    elif operator == 'minus':
        return 0 - operand
    elif operator == 'mul':
        return 0
    elif operator == 'div':
        return 0


def one(*operation: tuple) -> int:  # your code here
    if not len(operation): return 1

    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 1 + operand
    elif operator == 'minus':
        return 1 - operand
    elif operator == 'mul':
        return 1 * operand
    elif operator == 'div':
        return int(1 / operand)


def two(*operation: tuple) -> int:  # your code here
    if not len(operation): return 2
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 2 + operand
    elif operator == 'minus':
        return 2 - operand
    elif operator == 'mul':
        return operand * 2
    elif operator == 'div':
        return int(2 / operand)


def three(*operation: tuple) -> int:  # your code here
    if not len(operation): return 3
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 3 + operand
    elif operator == 'minus':
        return 3 - operand
    elif operator == 'mul':
        return operand * 3
    elif operator == 'div':
        return int(3 / operand)


def four(*operation: tuple) -> int:  # your code here
    if not len(operation): return 4
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 4 + operand
    elif operator == 'minus':
        return 4 - operand
    elif operator == 'mul':
        return operand * 4
    elif operator == 'div':
        return int(4 / operand)


def five(*operation: tuple) -> int:  # your code here
    if not len(operation): return 5
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 5 + operand
    elif operator == 'minus':
        return 5 - operand
    elif operator == 'mul':
        return operand * 5
    elif operator == 'div':
        return int(5 / operand)


def six(*operation: tuple) -> int:  # your code here
    if not len(operation): return 6
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 6 + operand
    elif operator == 'minus':
        return 6 - operand
    elif operator == 'mul':
        return operand * 6
    elif operator == 'div':
        return int(6 / operand)


def seven(*operation: tuple) -> int:  # your code here
    if not len(operation): return 7
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 7 + operand
    elif operator == 'minus':
        return 7 - operand
    elif operator == 'mul':
        return operand * 7
    elif operator == 'div':
        return int(7 / operand)


def eight(*operation: tuple) -> int:  # your code here
    if not len(operation): return 8
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 8 + operand
    elif operator == 'minus':
        return 8 - operand
    elif operator == 'mul':
        return operand * 8
    elif operator == 'div':
        return int(8 / operand)


def nine(*operation: tuple) -> int:  # your code here
    if not len(operation): return 9
    operation = operation[0]

    operator, operand = operation

    if operator == 'plus':
        return 9 + operand
    elif operator == 'minus':
        return 9 - operand
    elif operator == 'mul':
        return operand * 9
    elif operator == 'div':
        return int(9 / operand)


def plus(numFunc):
    return 'plus', numFunc


def minus(numFunc):
    return 'minus', numFunc


def times(numFunc):
    return 'mul', numFunc


def divided_by(numFunc):
    return 'div', numFunc
