import time
import naive
import finite_automaton


def measure_time_return(fun, text, pattern):
    start_time = time.time()
    res = fun(text, pattern)
    end_time = time.time()
    return end_time - start_time, res

def measure_time(fun, text, pattern):
    time, _ = measure_time_return(fun, text, pattern)
    return time


def generate_long_text(length):
    s = ""
    pattern = "aaaaaaaaaaaaa"
    for _ in range(length - len(pattern)):
        s += "b"
    s += "aaaaaaaaaaaaa"
    return s, pattern