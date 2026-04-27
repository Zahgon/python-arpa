from abc import ABCMeta, abstractmethod

UNK = '<unk>'
SOS = '<s>'
EOS = '</s>'


class ARPAModel(metaclass=ABCMeta):
    def __init__(self, unk=UNK):
        self._base = 10
        self._unk = unk

    def __contains__(self, word):
        self._check_word(word)
        return word in self.vocabulary()

    def __len__(self):
        return len(self.vocabulary())

    @abstractmethod
    def add_count(self, order, count):  # pragma: no cover
        pass

    @abstractmethod
    def add_entry(self, ngram, p, bo=None, order=None):  # pragma: no cover
        pass

    def log_p(self, ngram):
        pass

    def log_p_raw(self, ngram):
        pass

    def log_s(self, sentence, sos=SOS, eos=EOS):
        pass

    def p(self, ngram):
        pass

    def s(self, sentence):
        pass

    @abstractmethod
    def counts(self):  # pragma: no cover
        pass

    @abstractmethod
    def order(self):  # pragma: no cover
        pass

    @abstractmethod
    def vocabulary(self, sort=True):  # pragma: no cover
        pass

    def write(self, fp):
        pass

    @abstractmethod
    def _entries(self, order):  # pragma: no cover
        pass

    @abstractmethod
    def _log_bo(self, ngram):  # pragma: no cover
        pass

    @abstractmethod
    def _log_p(self, ngram):  # pragma: no cover
        pass

    @staticmethod
    def _check_input(input):
        pass

    @staticmethod
    def _check_word(input):
        pass

    def _replace_unks(self, words):
        pass
