from .base import *

try:
    from .local import *
except ImportError as exc:
    exc.args = tuple(['%s (did you created own local.py?)' %
                      exc.args[0]])
    raise exc
