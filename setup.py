from setuptools import setup, find_packages

version = '1.1.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name             = 'pyprnt',
    version          = version,
    description      = 'Python Pretty Printer',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author           = 'Kevin Kim',
    author_email     = 'kevink1103@gmail.com',
    license          = 'MIT',
    url              = 'https://github.com/kevink1103/pyprnt',
    download_url     = 'https://github.com/kevink1103/pyprnt/dist/pyprnt-{}.tar.gz'.format(version),
    install_requires = [],
    packages         = find_packages(exclude = []),
    keywords         = ['pretty', 'print'],
    python_requires  = '>=3',
    zip_safe         = False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)