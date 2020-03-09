import time
import naive
import finite_automaton


def measure_time(fun, text, pattern):
    start_time = time.time()
    fun(text, pattern)
    end_time = time.time()
    return end_time - start_time


def generate_long_text(length):
    s = ""
    pattern = "aaaaaaaaaaaaa"
    for _ in range(length - len(pattern)):
        s += "b"
    s += "aaaaaaaaaaaaa"
    return s, pattern