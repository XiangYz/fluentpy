def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count , total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager2()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(len(avg.__closure__))
    print(avg.__closure__[0].cell_contents)
    print(avg.__closure__[1].cell_contents)