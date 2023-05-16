#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in num_list if i % 2 == 0]
    # evens = [ i % 2 == 0 for i in num_list] returns booleans
    # for i in num_list:
    #     return [i if i % 2 == 0 else []]
    # for i in (num_list):
    #     evens = []
    #     if i % 2 == 0:
    #         evens.append(i)
    #     return evens


print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    return [i + "!" for i in sentence_list]
