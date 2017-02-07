
try:
    x = 2
    x()
except TypeError as e:
    print('TypeError', e, x)
    try:
        1 / 0
    except Exception as e:
        print('Ouch', e, type(e))
