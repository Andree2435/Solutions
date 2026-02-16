"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return ' :: '.join([prefix] + words_with_prefix)



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if word.endswith('ness'):
        new_word = word[:-4]
        if new_word.endswith('i'):
            new_word = new_word[:-1] + 'y'
    return new_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    word = sentence.split()[index].strip('.,!?').lower()
    return word + 'en'
