#!/usr/bin/python


def get_file_as_num_list(file):
    lines = list()
    with open(file, 'r') as f:
        for line in f:
            line = line.replace('\n', "")
            lines.append(int(line))
    return lines
