#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence == "":
        return (0, None)

    length = len(sentence)

    return (length, sentence[0])
