import os
import time
from random import randint


def log(fct):
    def new_fct(*arg, **kwargs):
        f = open("machine.log", "a")
        string_to_print = \
            "({0})Running: {1: <20}\t".format(os.getenv("USER"),
                                              fct.__name__.replace("_", " "))
        start = time.time()
        returned_value = fct(*arg, **kwargs)
        end = time.time()
        exec_time = end - start
        if exec_time < 1:
            string_to_print += (
                "[ exec-time = {0:.3f} ms ]\n".format(exec_time * 1000))
        else:
            string_to_print += (
                "[ exec-time = {0:.3f} s  ]\n".format(end - start))
        f.write(string_to_print)
        f.close()
        return returned_value
    return new_fct
