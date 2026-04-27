import gzip

from io import StringIO

from .models.simple import ARPAModelSimple
from .parsers.quick import ARPAParserQuick


def dump(obj, fp):
    """Serialize obj to fp (a file-like object) in ARPA format."""
    pass


def dumpf(obj, path, encoding=None):
    """Serialize obj to path in ARPA format (.arpa, .gz)."""
    pass


def dumps(obj):
    """Serialize obj to an ARPA formatted str."""
    pass


def load(fp, model=None, parser=None):
    """Deserialize fp (a file-like object) to a Python object."""
    pass


def loadf(path, encoding=None, model=None, parser=None):
    """Deserialize path (.arpa, .gz) to a Python object."""
    pass


def loads(s, model=None, parser=None):
    """Deserialize s (a str) to a Python object."""
    pass
