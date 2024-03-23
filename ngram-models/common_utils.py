from typing import List, Tuple, Dict
from collections import defaultdict
from constants import *

def build_basic_ngram(tokens: List[str], n:int) -> List[Tuple[str]]:
    ans = []
    for i in range(len(tokens)-n+1):
        start, end = i, i+n
        ans.append(tuple(tokens[start:end]))
    return ans

def build_ngrams_ctrl(tokens: List[str], n: int) -> List[Tuple[str]]:
    append_len = n-1
    appended_tokens = [BOS]*append_len + tokens + [EOS]*append_len
    return build_basic_ngram(tokens=appended_tokens, n=n)

def count_frequencies(texts: List[List[str]], n:int, verbose=False) -> Dict[Tuple[str], Dict[str, int]]:
    frequencies = dict()
    vocabularies = set()
    for tokens in texts:
        ngrams = build_ngrams_ctrl(tokens=tokens, n=n)
        vocabularies.update(set(tokens))
        for ngram in ngrams:
            context, token = ngram[:-1], ngram[-1]
            if verbose: print(f"context={context}, token={token}")
            if context in frequencies:
                frequencies[context][token] += 1
            else:
                frequencies[context] = defaultdict(int)
                frequencies[context][token] = 1
        # There maybe or may not be a context available -> How to reduce the if-else here? 
    return frequencies, vocabularies

def build_ngram_model(texts: List[List[str]], n:int, verbose=False) -> Dict[Tuple[str], Dict[str, float]]:
    ngram_counts, vocabularies = count_frequencies(texts=texts, n=n, verbose=verbose)
    ngram_model = dict()
    for context, count_dict in ngram_counts.items():
        total_count = sum(count_dict.values())
        freq = dict()
        for token, count in count_dict.items():
            freq[token]=count / total_count
        ngram_model[context]=freq
    return ngram_model, vocabularies