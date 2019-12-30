#!/usr/bin/python


def div_by_2(n):
    if type(n) != list:
        return None
    results = list()
    for i in n:
        results.append(int(i/2))
    return results

