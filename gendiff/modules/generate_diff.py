#!/usr/bin/env/python3
from gendiff.modules.return_stylish import stylish


def generate_diff(file1, file2, formatter='stylish'):
    if formatter == 'stylish':
        return stylish(file1, file2)


if __name__ == '__main__':
    generate_diff()
