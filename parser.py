import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S
NP -> N | Det N | Det Adj N | Adj N | NP PP
VP -> V | V NP | V NP PP | V PP | Adv VP | VP Adv
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # If a filename is provided, read the sentence from the file;
    # otherwise, prompt the user.
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()
    else:
        s = input("Sentence: ")

    # Preprocess the sentence: lowercase, tokenize, and remove non-alphabetic tokens.
    s = preprocess(s)

    # Attempt to parse the sentence using the defined grammar.
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return

    if not trees:
        print("Could not parse sentence.")
        return

    # For each parse tree, print the tree and then print all noun phrase chunks.
    for tree in trees:
        tree.pretty_print()
        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process the sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Tokenize the sentence (after lowercasing)
    tokens = nltk.word_tokenize(sentence.lower())
    # Filter out tokens that don't have any alphabetic characters
    words = [token for token in tokens if any(c.isalpha() for c in token)]
    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain other noun phrases
    as subtrees.
    
    For each subtree with label "NP", we check if none of its proper subtrees
    (excluding itself) are labeled "NP". If so, we include it as a chunk.
    """
    chunks = []
    for subtree in tree.subtrees(lambda t: t.label() == "NP"):
        # Check if this NP does NOT have any other NP as a proper descendant.
        if not any(child.label() == "NP" for child in subtree.subtrees(lambda t: t != subtree)):
            chunks.append(subtree)
    return chunks


if __name__ == "__main__":
    main()
