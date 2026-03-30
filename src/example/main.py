import argparse

from example.combine import combine_strings

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="example", description="Combine strings!")
    parser.add_argument("strings", nargs="*")
    parser.add_argument("--print", action="store_true")
    return parser

def main(args=None):
    parser = make_parser()
    parsed_args = parser.parse_args(args)

    result = combine_strings(*parsed_args.strings)

    if parsed_args.print:
        print(tuple(parsed_args.strings))
    print(result)