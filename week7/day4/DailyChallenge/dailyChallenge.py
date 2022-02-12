def divide_by_zero():
    try:
        return 5 / 0
    except ZeroDivisionError as e:
        print(f"You cannot divid a number by 0!!!: {e}")
    except Exception:
        print('You have got an Exception.')
    finally:
        print('"Final message will be here..."')


divide_by_zero()
