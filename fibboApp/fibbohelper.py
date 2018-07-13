def makeFibboSeries(num):
    a, b = 0, 1
    for _ in xrange(num):
        yield a
        a, b = b, a + b