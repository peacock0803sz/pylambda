from setuptools import find_packages
from setuptools import setup
setup(
    name='pylambda',
    version="0.1.0",
    description='',
    long_description='',
    install_requires=[
        'python-lambda',
    ],
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
        'flake8',
        'mypy',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)