from distutils.core import setup

setup(
    name = 'urlrap',
    packages = ['urlrap'], # this must be the same as the name above
    version = '0.1',
    description = 'URL connivance functions.',
    author = 'Bob Colner',
    author_email = 'bcolner@gmail.com',
    url = 'https://github.com/bobcolner/urlrap', 
    download_url = 'https://github.com/bobcolner/urlrap/tarball/0.1',
    keywords = ['url', 'utility'], # arbitrary keywords
    license = 'MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
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
    install_requires = ['urltools']
)
