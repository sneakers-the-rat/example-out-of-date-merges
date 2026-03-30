import argparse

from example.combine import combine_strings

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="example", description="Combine strings!")
    parser.add_argument("strings", nargs="*")
    return parser

def main(args=None):
    parser = make_parser()
    parsed_args = parser.parse_args(args)

    result = combine_strings(*parsed_args.strings)

    print(result)