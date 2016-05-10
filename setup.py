from setuptools import find_packages, setup

VERSION = '0.4'

setup(
    name = 'urlrap',
    packages = find_packages(),
    version = VERSION,
    platforms=["any"],
    description = 'URL connivance functions.',
    author = 'Bob Colner',
    author_email = 'bcolner@gmail.com',
    url = 'https://github.com/bobcolner/urlrap', 
    download_url = 'https://github.com/bobcolner/urlrap/tarball/{0}'.format(VERSION),
    keywords = ['url', 'utility'], # arbitrary keywords
    license = 'MIT',
    classifiers = [ # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet',
        # Pick your license as you wish (should match 'license' above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    test_suite = 'tests'
)
