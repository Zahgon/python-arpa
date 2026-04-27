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
        fp.write('\n\\data\\\n')
        for order, count in self.counts():
            fp.write('ngram {}={}\n'.format(order, count))
        fp.write('\n')
        for order, _ in self.counts():
            fp.write('\\{}-grams:\n'.format(order))
            for e in self._entries(order):
                prob = e[0]
                ngram = ' '.join(e[1])
                if len(e) == 2:
                    fp.write('{}\t{}\n'.format(prob, ngram))
                elif len(e) == 3:
                    backoff = e[2]
                    fp.write('{}\t{}\t{}\n'.format(prob, ngram, backoff))
                else:
                    raise ValueError
            fp.write('\n')
        fp.write('\\end\\\n')

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
