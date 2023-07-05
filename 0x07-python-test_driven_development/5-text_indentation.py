#!/usr/bin/python3


'''
  Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.
'''


def text_indentation(text):
    """

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    period = text.replace('.', '.\n\n')
    period = period.replace('?', '?\n\n')
    period = period.replace(':', ':\n\n')
    period1 = period.split('\n')
    for line in range(len(period1)):
        print("{}".format(period1[line].strip()),
              end=("" if (line == (len(period1) - 1)) else '\n'))
