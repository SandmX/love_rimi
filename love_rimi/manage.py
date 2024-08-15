import argparse

from . import __version__
from .this_un import this_un


def main():
    parser = argparse.ArgumentParser(description='Check if package is installed correctly')
    parser.add_argument('-V', '--version', action='version', version=f'{__version__}')
    parser.add_argument('-lang', type=str, help='specify the language of words')

    args = parser.parse_args()

    if args.lang:
        this_un.this(args.lang)
    else:
        from love_rimi import this

