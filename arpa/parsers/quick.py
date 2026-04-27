from enum import Enum, unique
import re

from .base import ARPAParser
from ..exceptions import ParseException


class ARPAParserQuick(ARPAParser):
    @unique
    class State(Enum):
        DATA = 1
        COUNT = 2
        HEADER = 3
        ENTRY = 4

    re_count = re.compile(r'^ngram (\d+)=(\d+)$')
    re_header = re.compile(r'^\\(\d+)-grams:$')
    re_entry = re.compile('^(-?\\d+(\\.\\d+)?([eE]-?\\d+)?)'
                          '\t'
                          '(\\S+( \\S+)*)'
                          '(\t(-?\\d+(\\.\\d+)?)([eE]-?\\d+)?)?$')

    def __init__(self, model):
        self.ModelClass = model

    def parse(self, fp):
        pass

    def _data(self, line):
        pass

    def _count(self, line):
        pass

    def _header(self, line):
        pass

    def _entry(self, line):
        pass

    @staticmethod
    def _float_or_int(s):
        pass
