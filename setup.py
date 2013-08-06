from setuptools import setup
import os
from distutils.command.install import INSTALL_SCHEMES


core_files = []
for dirname, dirnames, filenames in os.walk('common/'):
    dirfiles = [os.path.join(dirname, filename) for filename in filenames]
    core_files.append((dirname, dirfiles))

current_directory = os.path.abspath(os.path.dirname(__file__))
readme_name = os.path.join(current_directory, "pybindings", "README.md")
readme_text = open(readme_name).read()

data_files = core_files

setup_args = {
    'name': 'dali',
    'maintainer': '2gis',
    'maintainer_email': 'autoqa@2gis.ru',
    'version': "0.1",
    'license': 'MIT',
    'description': 'Python bindings for Dali - selenium-based webpage screenshot comparison tool',
    'long_description': readme_text,
    'url': 'https://github.com/2gis/dali.git',
    'packages': {'dali',
    },
    'package_dir': {
        'dali': 'pybindings/dali',
    },
    'data_files': data_files,
    'install_requires': [
        'thrift==0.9.0',
        'selenium==2.33.0',
        'numpy==1.7.1',
    ],
}

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib'] + '/' + list(setup_args['packages'])[0]

setup(**setup_args)