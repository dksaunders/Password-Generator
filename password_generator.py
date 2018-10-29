#!/usr/bin/env python3

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
    word_count = 0

    try:
        word_count = int(argv[1])
    except IndexError:
        raise IndexError(
            'Pass in the number of words to include in the password.')
    except ValueError:
        raise ValueError('The argument passed must be an integer value.')

    password = '-'.join(word_list(word_count))
    print(password)


if __name__ == '__main__':
    from sys import argv
    main()
