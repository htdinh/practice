import re
import string

# Compute the weight of alphabet and store in a dictionary {"a":1,...,"z":26}
alphabets = list(string.ascii_lowercase)
weights = {}
for idx, letter in enumerate(alphabets):
    weights[letter] = idx+1


def get_weight(s):
    """
    :param s: input string i.e. "abccddde"
    :return: set of weights for uniform_substring
    """
    global weights  # reuse the alphabet weights for each letter "a", "b", etc.
    uni_weights = set()
    for match in re.finditer(r"(\w)\1*", s):  # using Regular expression seems faster (and much simpler check)
        letter = s[match.start()]
        letter_weight = weights[letter]
        length = match.end()-match.start()
        uni_weights.update([i*letter_weight for i in range(1,length+1)])
    return uni_weights

s = raw_input().strip()
uni_weights = get_weight(s)
n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())
    # your code goes here
    if x in uni_weights:
        print "Yes"
    else:
        print "No"
