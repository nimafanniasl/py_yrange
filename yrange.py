def yrange(max, min = None):
    if min != None:
        num = min
    else:
        num = 0
    while (num<max):
        yield num
        num += 1