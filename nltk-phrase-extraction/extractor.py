from nltk.corpus import stopwords
import nltk

sentence_re = \
    r'''(?x)      # set flag to allow verbose regexps
      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*            # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
    | \.\.\.                # ellipsis
    | [][.,;"'?():-_`]      # these are separate tokens
'''

lemmatizer = nltk.WordNetLemmatizer()
# stemmer = nltk.stem.porter.PorterStemmer()

grammar = \
    r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""

chunker = nltk.RegexpParser(grammar)

stopwords = stopwords.words('english')

# Finds NP (noun phrase) leaf nodes of a chunk tree.
def leaves(tree):
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        yield subtree.leaves()


# Normalises words to lowercase and stems and lemmatizes it.
def normalise(word):
    word = word.lower()
    # word = stemmer.stem_word(word)
    word = lemmatizer.lemmatize(word)
    return word


# Checks conditions for acceptable word: length, stopword.
def acceptable_word(word):
    accepted = bool(2 <= len(word) <= 40 and word.lower()
                    not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [normalise(w) for (w, t) in leaf if acceptable_word(w)]
        yield term
    