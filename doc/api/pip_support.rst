.. currentmodule:: jnrbase.pip_support

pip_support
===========

.. autofunction:: parse_requires

Examples
--------

.. testsetup::

    from jnrbase.pip_support import parse_requires

.. doctest::

    >>> parse_requires('extra/requirements-test.txt')
    ['click>=3.0', 'configobj>=0.5.0', 'ciso8601>=1.0.1', 'pytz', 'httplib2', 'html2text', 'Jinja2>=2', 'Pygments', 'expecter>=0.2.2', 'hiro>=0.1.7', 'nose2[coverage_plugin]>=0.5.0']
