#!/usr/bin/env python3

import argparse
from random import randrange


def dice(count: int = 5, sides: int = 6) -> list:
    return [randrange(1, sides+1) for _ in range(count)]


def lookup(dice_roll: list) -> str:
    dice_roll = ''.join(str(x) for x in dice_roll)

    with open('eff_large_wordlist.txt', 'r') as words:
        for line in words:
            dice_index, word = line.split('\t')
            if int(dice_index == dice_roll):
                return word.strip('\n')

    raise IndexError('Index not in Word List.')


def word_list(words: int) -> list:
    for _ in range(words):
        yield lookup(dice())


def main():
    parser = argparse.ArgumentParser(
        prog='(Virtual) Diceware Password Generate',
        description='A program that rolls virtual dice to generate a passphrase.'
    )
    parser.add_argument(
        'words',
        type=int,
        help='number of words in the password'
    )
    parser.add_argument(
        '-s', '--separator',
        type=str,
        default='-',
        help='character to separate words'
    )
    args = parser.parse_args()

    password = args.separator.join(word_list(args.words))
    print(password)


if __name__ == '__main__':
    from sys import argv
    main()
