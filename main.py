#! /usr/bin/env python
"""Text analysis and reporting script"""


def count_words(s: str) -> int:
    """Count words in s"""
    return len(s.split())


def count_letters(s: str):
    """Count unique letters in s

    Non-alpha letters are ignored. Ignores case.
    """
    counter = {}
    for char in s:
        if not char.isalpha():
            continue
        char = char.lower()
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    return counter


def print_report(path: str, num_words: int, letters: dict) -> None:
    """Print report."""
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char in sorted(letters.keys()):
        print(f"The '{char}' character was found {letters[char]} times")


def main():
    """Script main entry point"""
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        letters = count_letters(file_contents)
        print_report(path, num_words, letters)


main()
