#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['jinja2']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

install_requires = \
['MarkupSafe>=2.0']

extras_require = \
{'i18n': ['Babel>=2.7']}

entry_points = \
{'babel.extractors': ['jinja2 = jinja2.ext:babel_extract[i18n]']}

setup(name='Jinja2',
      version='3.1.4',
      description='A very fast and expressive template engine.',
      author=None,
      author_email=None,
      url=None,
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.7',
     )
