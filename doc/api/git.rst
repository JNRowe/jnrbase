.. currentmodule:: jnrbase.git

git
===

.. autofunction:: find_tag

Examples
--------

.. testsetup::

    from jnrbase.git import find_tag
    from tests.test_git import tarball_data

.. doctest::

    >>> with tarball_data('semver') as tree:
    ...    find_tag(git_dir=tree)
    'v2.3.4'
