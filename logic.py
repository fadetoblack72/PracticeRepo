#Short function that evaluates boolean logic

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        if x == 0 or y == 0:
            return 0
        return 1
    elif operation == OPERATION_NAMES[1]:
        if x == 0 and y == 0:
            return 0
        return 1
    elif operation == OPERATION_NAMES[2]:
        if x == 1:
            return y
        return 1
    elif operation == OPERATION_NAMES[3]:
        return ((x + y) % 2)
    else:
        if x == y:
            return 1
        return 0