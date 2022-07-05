#!/usr/bin/python3
""" Defines the method append_write """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename: path to file
        text: string to be appended

    Returns:
        returns the number of characters appended
    """
    with open(filename, mode='a', encoding='utf-8') as file_a:
        a_file = file_a.write(text)
        return a_file
