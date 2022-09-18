Changelog
=========

1.5 - 2022-09-18
----------------

- Allow type checkers to infer the type of a lazy attribute.
  Thanks to Elias Keis and Palpatineli for their contributions.
  [elKei24] [Palpatineli]

- Add Python 3.8-3.11 to tox.ini. Remove old Python versions.
  [stefan]

- Replace deprecated ``python setup.py test`` in tox.ini.
  [stefan]

- Remove deprecated ``test_suite`` from setup.py.
  [stefan]

- Move metadata to setup.cfg and add a pyproject.toml file.
  [stefan]

- Include tests in sdist but not in wheel.
  [stefan]

1.4 - 2019-01-28
----------------

- Add MANIFEST.in.
  [stefan]

- Release as universal wheel.
  [stefan]

1.3 - 2017-02-05
----------------

- Support Python 2.6-3.6 without 2to3.
  [stefan]

- Add a LICENSE file.
  [stefan]

1.2 - 2014-04-19
----------------

- Remove setuptools from install_requires because it isn't.
  [stefan]

1.1 - 2012-10-12
----------------

- Use ``functools.wraps()`` properly; the list of attributes changes with
  every version of Python 3.
  [stefan]

1.0 - 2011-03-24
----------------

- Initial release.
