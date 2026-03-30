def combine_strings(*strings: str, sep: str = ".", print_strings:bool=True)->str:
    if print_strings:
        print(strings)
    return sep.join(strings)
