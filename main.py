from time import time


def number_to_pow(num_pow=2, *numbers):
    return list(map(lambda num: num ** num_pow, numbers))


print(number_to_pow(3, 2, 3, 4))


def time_func(func, *args):
    # print("timing func", func, "with args", args)
    start_time = time()
    print("time before", start_time)
    res = func(*args)
    end_time = time()
    print("time after", end_time)
    print("computed in", end_time - start_time)
    # print("returning result", res)
    return res


def time_dec(func):
    def wrapper(*args):
        return time_func(func, *args)
    return wrapper


@time_dec
def odd_or_even(num_list, type):
    def num_filter(num):
        if type == 'even':
            return num % 2 == 0
        else:
            return num % 2 != 0

    return list(filter(num_filter, num_list))


my_num_list = list(range(1, 1_000_000_000))
odd_or_even(my_num_list, 'odd')
