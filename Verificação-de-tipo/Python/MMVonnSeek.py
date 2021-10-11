def only_ints(x, y):
    number = 1

    if type(x) == type(number) and type(y) == type(number):
       return True
    else:
        return False

only_ints(1, 2)
