def progression(start, step):
    while True:
        yield start
        start *= step

