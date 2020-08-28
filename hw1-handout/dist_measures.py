"""Calculate information-theoretic measures of distributional
similarity based on word frequencies in two texts
"""

import collections
import math


def read_words(infile):
    with open(infile) as input_text:
        return [x.strip() for x in input_text.read().split()]


def get_counts(word_list):
    return collections.Counter(word_list)


def create_prob_dist(count_dict):
    total_ct = sum(count_dict.values())
    p = {x: ct / total_ct for x, ct in count_dict.items()}
    return p


def count_smoothing(freq_dist, vocabulary, alpha=1):
    """Implement simple count-based probability smoothing.
    Given a target vocabulary and a set of observed count frequencies,
    calculate a new set of counts so that Count(x) > 0 for all words
    in the target vocabulary.  This is achieved by adding `alpha`
    to each observed count
    """
    return {w: freq_dist.get(w, 0) + alpha for w in vocabulary}


def entropy(p):
    """Calculate entropy H(p) for a probability distribution represented
    as a mapping (dictionary) from word tokens to probabilities
    """
    # create an array of (probability * ln(probability)) through iterating all the words in word->probability map
    h = [(p.get(x, 0)*math.log(p.get(x, 0))) for x in p.keys()]
    # calculate sum of all the elements in above array
    h = sum(h)
    # return negative value of the above sum which is an entropy
    return -h


def cross_entropy(p1, p2):
    """Calculate cross-entropy H(p1, p2) for two probability distributions
    represented as a mapping (dictionary) from word tokens to
    probabilities
    """
    # here both probability distribution has same set of words as keys
    # create an array of (probability1 * ln(probability2)) through iterating all the words in word->probability map
    xh = [(p1.get(x, 0)*math.log(p2.get(x, 0))) for x in p1.keys()]
    # calculate sum of all the elements in above array
    xh = sum(xh)
    # return negative value of the above sum which is an cross_entropy
    return -xh


def kl_divergence(p1, p2):
    """Calculate Kullback-Leibler divergence D_{KL}(p1||p2) for two
    probability distributions represented as a mapping (dictionary)
    from word tokens to probabilities
    """
    # here both probability distribution has same set of words as keys
    # create an array of (probability1 * ln(probability2/probability1)) through iterating all the words in word->probability map
    kl = [(p1.get(x, 0)*math.log(p2.get(x, 0)/p1.get(x, 0))) for x in p1.keys()]
    # calculate sum of all the elements in above array
    kl = sum(kl)
    # return negative value of the above sum which is kl-divergence
    return -kl


def js_divergence(p1, p2):
    """Calculate Jensen-Shannon divergence D_{JS}(p1||p2) for two
    probability distributions represented as a mapping (dictionary)
    from word tokens to probabilities
    """
    # here both probability distribution has same set of words as keys
    # create a map of word->((probability1+probability2)/2) which is an average probability distribution (m)
    m = {x: ((p1.get(x, 0) + p2.get(x, 0))/2.0) for x in p1.keys()}
    # calculate average of kl-divergence(p1,m) and kl-divergence(p2,m)
    js = (kl_divergence(p1, m) + kl_divergence(p2, m))/2.0
    # return above value which is js-divergence
    return js


if __name__ == "__main__":
    """Do not edit this code
    """
    words_a = read_words("test_a.txt")
    words_b = read_words("test_b.txt")

    ct_a = get_counts(words_a)
    ct_b = get_counts(words_b)

    vocab = set(ct_a.keys()) | set(ct_b.keys())
    ct_a = count_smoothing(ct_a, vocab)
    ct_b = count_smoothing(ct_b, vocab)

    p_a = create_prob_dist(ct_a)
    p_b = create_prob_dist(ct_b)

    h_a = entropy(p_a)
    h_b = entropy(p_b)
    xh_ab = cross_entropy(p_a, p_b)
    xh_ba = cross_entropy(p_b, p_a)
    kl_ab = kl_divergence(p_a, p_b)
    kl_ba = kl_divergence(p_b, p_a)
    js_ab = js_divergence(p_a, p_b)
    js_ba = js_divergence(p_b, p_a)

    for metric in [h_a, h_b, xh_ab, xh_ba,
                   kl_ab, kl_ba, js_ab, js_ba]:
        print("{:.3f}".format(metric))
