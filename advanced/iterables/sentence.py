"""Module implements Sentence class"""

import re


def remove_empty_strings(strings):
    """Util for remove empty elements from strings"""
    return list(filter(lambda s: s != '', strings))


def count_sentences(text):
    """Util for count sentences in text"""
    sentences = [text]

    for delimiter in ['.', '...', '!', '?']:
        new_sentences = []
        for sentence in sentences:
            new_sentences = new_sentences + remove_empty_strings(sentence.split(delimiter))
        sentences = new_sentences

    return len(sentences)


def get_words(string):
    """Returns words from the text"""
    return re.findall(r'[a-zA-Z]+', string)


def get_non_words(string):
    """Return non words from the text"""
    return re.findall('[^a-zA-Z ]', string)


def count_words(string):
    """Counting words in the text"""
    return len(get_words(string))


def count_non_words(string):
    """Counting non words in the text"""
    return len(get_non_words(string))


class MultipleSentencesError(Exception):
    """Custom Exception raises when detected more than one sentences in the text"""


class Sentence:
    """Sentence class"""

    def __init__(self, sentence):
        self.sentence = sentence

        self._validate_type()
        self._validate_complete_sentence()
        self._validate_sentences_count()

    @property
    def _count_words(self):
        """Count of words in the sentence"""
        return count_words(self.sentence)

    @property
    def _count_other_chars(self):
        """Count of other characters in the sentence"""
        return count_non_words(self.sentence)

    def _words(self):
        """Returns generator of words"""
        for word in get_words(self.sentence):
            yield word

    @property
    def words(self):
        """List of words"""
        return list(self._words())

    @property
    def other_chars(self):
        """List of other characters"""
        return get_non_words(self.sentence)

    def __getitem__(self, item):
        return self.words[item]

    def _validate_type(self):
        """Validataing sentence type"""
        if not isinstance(self.sentence, str):
            raise TypeError('Sentence accepts only strings.')

    def _validate_complete_sentence(self):
        """Validataing sentence for completing"""
        is_complete = False

        for ending in ['.', '...', '!', '?']:
            if self.sentence.endswith(ending):
                is_complete = True

        if not is_complete:
            raise ValueError('Sentence have to be completed.')

    def _validate_sentences_count(self):
        """Validating sentence for count"""
        if count_sentences(self.sentence) > 1:
            raise MultipleSentencesError('Only one sentence allowed.')

    def __repr__(self):
        return f'Sentence(words={self._count_words}, other_chars={self._count_other_chars})'

    def __iter__(self):
        return SentenceInterator(self.words)


class SentenceInterator:
    """Class Iterator for sentence"""

    def __init__(self, words):
        self._words = words
        self._length = len(self._words)
        self._remains = self._length

    def __next__(self):
        if self._remains > 0:
            self._remains -= 1
            return self._words[self._length - self._remains - 1]
        raise StopIteration

    def __iter__(self):
        return self
