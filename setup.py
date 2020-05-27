import setuptools

setuptools.setup(
    name='google-foobar',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    extras_require={
        'test': [
            'bandit',
            'flake8',
            'pylint',
            'pytest-cov',
            'pytest-xdist'
        ]
    }
)
