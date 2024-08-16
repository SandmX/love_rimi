from rich.console import Console
from rich.table import Table

import argparse

from . import __version__


console = Console()


def default_action():
    from . import this

def show_lang_list() -> None:
    from .this_un import check

    lang = check.lang_list()

    ava_display_rule = {
        True: '[green]✓[/]',
        False: '[red]✕[/]'
    }
    lang_table = Table(show_header=True, header_style="bold magenta", title="language files list")
    lang_table.add_column("[yellow]name[/]")
    lang_table.add_column("available", justify="center")

    for name, available in lang.items():
        lang_table.add_row(name, ava_display_rule[available])

    console.print(lang_table)


def main():
    parser = argparse.ArgumentParser(description='Check if package is installed correctly')
    parser.add_argument('-V', '--version', action='version', version=f'{__version__}')
    parser.add_argument('-lang', type=str, help='specify the language of words')
    parser.add_argument('--lang-list', action='store_true', help='show the list of available .lang files')
    parser.add_argument('-where', action='store_true', help='show the directory where .lang files are located')

    args = parser.parse_args()

    if all(v in [None, False] for v in vars(args).values()):
        default_action()
    if args.lang:
        from .this_un import this_un
        this_un.this(args.lang)
    if args.lang_list:
        show_lang_list()
    if args.where:
        from .this_un.check import where
        print('language files are located in:\n', where())

