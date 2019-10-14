#!/usr/bin/env python3

import argparse
from random import randrange


def dice(count=5, sides=6):
    return [randrange(1, sides+1) for _ in range(count)]


def lookup(index):
    index = ''.join(str(x) for x in index)

    with open('eff_large_wordlist.txt', 'r') as words:
        for line in words:
            element = line.split('\t')
            if int(element[0] == index):
                return element[1].strip('\n')

    raise IndexError('Index not in Word List.')


def word_list(words, count=5, sides=6):
    for _ in range(words):
        yield lookup(dice(count, sides))


def main():
    parser = argparse.ArgumentParser(
        prog='(Virtual) Diceware Password Generate',
        description='A program that rolls virtual dice to generate a passphrase.'
    )
    parser.add_argument('words', type=int, help='number of words in the password')
    parser.add_argument('-s', '--separator', type=str, default='-', help='character to separate words')
    args = parser.parse_args()

    password = args.separator.join(word_list(args.words))
    print(password)


if __name__ == '__main__':
    from sys import argv
    main()
