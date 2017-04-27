# Setuptools is used to facilitate packaging
# Python projects.

from setuptools import setup, find_packages

setup(
    # Package details
    name = 'dluxAlgorithms',
    version = '1.0.0',
    packages = find_packages(),

    #metadata for upload to PyPI
    description = 'Packaging a python project which will contain algorithm code exercises',
    author = 'Luz Cazares',
    author_email = 'tmp@dlux.com',
    url = 'https://github.com/dlux/algorithms',
    test_suite='tests',
    keywords = ['dlux', 'algorithms', 'mypackage'],

    # Additional metadata
    classifier = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Quality Engineers',
        'Intended Audience :: Information Technology',
        'License :: Free For Educational Use',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        ],
    entry_points = {
         'console_scripts':[
             'dlux_alg = src.main:main',
             ],
         'dlux_alg.cm':[
             'quick_find = src.client_union_find:main',
             ]	
         }
)

