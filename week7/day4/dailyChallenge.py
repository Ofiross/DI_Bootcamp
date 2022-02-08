def divide_by_zero():
    try:
        return 5 / 0
    except ZeroDivisionError:
        print("You cannot divid a number by 0!!!")
    except Exception:
        print('You have got an Exception.')
    finally:
        print('Final message')


divide_by_zero()
