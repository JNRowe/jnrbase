.. currentmodule:: jnrbase.git

git
===

.. autofunction:: find_tag

Examples
--------

..
    Can't be a doctest without shipping a git tree for the test, or basically
    allowing it a full ellipsis match :/

.. code-block:: pycon

    >>> find_tag(strict=False)
    '4c411a98-dirty'
