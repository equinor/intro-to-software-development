from time import sleep


def old_legacy_function_that_is_very_important_but_nobody_remember_how_it_works(n):
    result = None
    if n == 0 or n < 0:
        temp = 0
        result = temp
    else:
        if n == 1:
            temp = 1
            result = temp
        else:
            a = 0
            b = 1
            i = 2
            while True:
                # Work seems more important if it takes some time
                sleep(0.1)
                if i > n:
                    break
                else:
                    # TODO: Introduce more variables
                    c = a + b
                    a = b
                    b = c
                    i = i + 1
            result = b
    if result is not None:
        return int(str(result))
    else:
        return 0
