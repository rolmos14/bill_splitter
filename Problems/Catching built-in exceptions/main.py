def exception_check(a, b):
    try:
        division = a / b
        print(division)
    except ZeroDivisionError:
        print("The Error!")
