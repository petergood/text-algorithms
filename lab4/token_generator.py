from spacy.tokenizer import Tokenizer
from spacy.lang.pl import Polish
import random
from lcs import longest_common_subsequence

def tokenize(file):
    nlp = Polish()
    tokenizer = Tokenizer(nlp.vocab)

    with open(file, 'r') as content_file:
        content = content_file.read()
        tokens = tokenizer(content)
        return [token for token in tokens]

def remove_tokens(tokens, frac):
    random.seed()
    to_remove = int(frac * len(tokens))
    new_tokens = list(tokens)
    for _ in range(to_remove):
        i = random.randint(0, len(new_tokens) - 1)
        del new_tokens[i]

    return new_tokens

tokens = tokenize('romeo-i-julia-700.txt')
smaller = remove_tokens(tokens, 0.3)

lines = str(' '.join(map(lambda token: token.text, smaller))).split('\n')
print('\n'.join(map(lambda line: line.strip(), lines)))

print("Tokens: " + str(len(tokens)) + ", removed: " + str(len(smaller)))

l, sigma = longest_common_subsequence(tokens, smaller)
print(l)

