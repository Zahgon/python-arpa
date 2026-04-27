from collections import OrderedDict

from .base import ARPAModel
from .base import UNK
from ..exceptions import FrozenException


class ARPAModelSimple(ARPAModel):
    def __init__(self, unk=UNK):
        super().__init__(unk=unk)
        self._counts = OrderedDict()
        self._ps = OrderedDict()
        self._bos = OrderedDict()
        self._vocabulary = None
        self._vocabulary_sorted = None

    def __contains__(self, word):
        self._check_word(word)
        return word in self.vocabulary(sort=False)

    def add_count(self, order, count):
        pass

    def add_entry(self, ngram, p, bo=None, order=None):
        pass

    def counts(self):
        pass

    def order(self):
        pass

    def vocabulary(self, sort=True):
        pass

    def _entries(self, order):
        pass

    def _entry(self, ngram):
        pass

    def _log_bo(self, ngram):
        pass

    def _log_p(self, ngram):
        pass
