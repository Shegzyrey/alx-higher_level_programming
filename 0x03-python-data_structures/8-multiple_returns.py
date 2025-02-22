#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if sentence_length == 0:
        first_letter = None
        return (sentence_length, first_letter)
    first_letter = sentence[0]
    return (sentence_length, first_letter)
