import argparse
from pathlib import Path


PKGS_FILE = Path('~/.config/pipus.txt').expanduser()


class HelpFormatter(argparse.HelpFormatter):
    def _get_help_string(self, action):
        if type(action) == argparse._StoreAction and action.default:
            return argparse.ArgumentDefaultsHelpFormatter._get_help_string(self, action)
        return super()._get_help_string(action)


parser = argparse.ArgumentParser(
    __package__,
    formatter_class=HelpFormatter,
    add_help=False,
)
parser.add_argument(
    'packages', nargs='*',
    help="Packages to install",
)

options = parser.add_argument_group('Options')
options.add_argument(
    '-f', '--file', default=PKGS_FILE, type=Path,
    help="Path to the packages file, in requirements-like format",
)
options.add_argument(
    '-y', '--yes', action='store_true',
    help="Assume yes and do not ask for confirmation before performing destructive actions",
)
options.add_argument(
    '--no-write', action='store_true',
    help="Do not update packages file",
)

commands = parser.add_argument_group('Commands')
commands.add_argument(
    '-u', '--update', action='store_true',
    help="Update all listed packages, that's the default when there is no argument",
)
commands.add_argument(
    '-l', '--list', action='store_true',
    help="List packages in packages file",
)
commands.add_argument(
    '-r', '--refresh', action='store_true',
    help="Removes all local packages and install the ones listed in the packages file instead",
)
commands.add_argument(
    '-R', '--remove', action='store_true',
    help='Uninstalls packages instead of installing',
)
commands.add_argument(
    '-h', '--help', action='store_true',
    help="Prints this message and exits",
)

args = parser.parse_args()
