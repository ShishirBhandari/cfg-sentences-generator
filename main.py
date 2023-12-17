import random
from grammar_parser import grammar_parser, get_rules
from constants import NUM_OF_SENTENCES, MAX_WORD_COUNT


def select_random_value(values: list[str]) -> str:
    """
    Given a list of values, it returns any one value randomly
    """
    return values[random.randint(0, len(values) - 1)]


def generate_sentence(rules: dict[str, list]) -> str:
    """
    Generates a sentence following given grammar rules
    """
    # initialize the random sentence from the ROOT and split into words
    sentence = select_random_value(rules["ROOT"])
    splitted = sentence.split()

    sentence_terminated = False
    while not sentence_terminated:
        # limit max word count to prevent infinite loop
        if len(splitted) > MAX_WORD_COUNT:
            sentence = select_random_value(rules["ROOT"])

        splitted = sentence.split()
        is_sentence_replaced = False
        # go through each word in the splitted sentence
        for word in splitted:
            # if the word is in the key of the rules, use the rule to replace it
            if word in rules:
                selected = select_random_value(rules[word])
                sentence = sentence.replace(word, selected, 1)
                is_sentence_replaced = True
        # if none of the word can be replaced, terminate the sentence and the loop
        if not is_sentence_replaced:
            sentence_terminated = True

    return sentence


def generate_sentences(
    rules: dict[str, list], num_sentences=NUM_OF_SENTENCES
) -> set[str]:
    """
    Generates a given number of sentences following the provided grammar rules
    """
    # set stores only unique values
    sentences = set[str]()

    i = 0
    while i < num_sentences:
        # generate a sentence
        sentence = generate_sentence(rules)
        # check if the sentence already exists i.e. duplicate
        if sentence in sentences:
            continue

        # if not duplicate, add the sentence to the final set
        sentences.add(sentence)
        i += 1

    return sentences


def write_sentences(out_file_path: str, sentences: set[str]):
    """
    Write sentences to the text file: out_file_path
    """
    with open(out_file_path, "w") as file:
        file.writelines("\n".join(sentences))


def main():
    """
    Entrypoint
    """
    # First of all, parse the grammar file
    parsed = grammar_parser("./grammar.gr", delimiter="\t")
    # Extract rules from the parsed grammar
    rules = get_rules(parsed)
    # Generate the sentences
    sentences = generate_sentences(rules, NUM_OF_SENTENCES)
    # Write sentences to the output file
    write_sentences("output.txt", sentences)


if __name__ == "__main__":
    main()
