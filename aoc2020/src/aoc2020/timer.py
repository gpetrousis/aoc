""" Performance utils """
import functools
from time import perf_counter_ns


def to_title(string):
    """ Replace _ with space and Capitilize first letter """
    return string.replace("_", " ").title()


def timer(func):
    """ Timer function to count execution time """

    @functools.wraps(func)
    def wrapper_benchmark(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        diff_ms = (end - start) / 10 ** 6
        return f"{result} [{diff_ms:.2f}ms]"

    return wrapper_benchmark
