.. currentmodule:: jnrbase.compat

compat
======

.. class:: basestring()

    Python 2 and 3 compatible basestring definition.

.. function:: text(object[, encoding[, errors]])

    Python 2 and 3 compatible text definition.

    On Python 2 this will be the :class:`Unicode` type, and on Python 3 the
    class:`str` type.

.. function:: StringIO()

    Python 2 and 3 compatible StringIO definition.

    On Python 2 this will be :func:`cStringIO.StringIO`, if it is available.

.. function:: open(file, mode='rb', encoding=None, errors='strict', buffering=1)

    Python 2 and 3 compatible :func:`open` definition.

    On Python 2 this uses :func:`codecs.open`, and Python 3 the standard
    :func:`open` function is used.

.. autofunction:: mangle_repr_type

    On Python 3 this is simply a no-op, as it is unnecessary.

.. autofunction:: safe_hasattr

    On Python 3 this is simply a no-op, as it is unnecessary.
