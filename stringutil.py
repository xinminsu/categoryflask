

def is_digital(str):
    res = ''.join([i for i in str if not i.isdigit()])
    if res and not res.isspace():
        return False
    else:
        return True