def grammar_parser(filepath: str, delimiter: str) -> list[list[str]]:
    """
    Reads .gr file and extracts the values
    """
    grammar = list[list[str]]()
    # open file to read
    with open(filepath, "r") as file:
        # read line by line
        for line in file.readlines():
            # remove comments and whitespaces
            line = line.split("#")[0].strip()
            # if the line is empty, then ignore the line
            if not line:
                continue

            # extract values from data
            line_values = line.split(delimiter)
            grammar.append(line_values)

    return grammar


def get_rules(grammar: list[list[str]]) -> dict[str, list]:
    """
    Extracts rules from parsed grammar
    e.g.
    input: ['1',   'ROOT',  'S .']
    output: {'ROOT': ['S .']}
    """
    rules = dict[str, list]()

    # loop through each line
    for line in grammar:
        # only consider 2nd and 3rd columns; 1st column can be ignored
        non_terminal = line[1]
        terminal = line[2]

        # use non_terminals as dictionary keys
        if non_terminal in rules:
            rules[non_terminal].append(terminal)
        else:
            rules[non_terminal] = [terminal]

    return rules
