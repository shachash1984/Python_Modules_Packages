#!/usr/bin/python
import sys
sys.path.append('E:\\Coding Projects\PythonProjects')
import ModuleWithEntryPoint
from PyMath import math_module as math
from PyFiles import file_handler_module as file_handler


def main():
    values = list(math.div_by_2(file_handler.get_file_as_num_list('nums.txt')))
    print(values)


if __name__ == "__main__":
    main()
