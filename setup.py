import os
import sys

from setuptools import setup

if sys.version_info < (2, 7) or sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 2.7 is not supported. Please use Python 3.7+.')

MAJOR_VERSION = 0
MINOR_VERSION = 0
REVISION = 2

PACKAGE_VERSION = '.'.join([
    str(item) for item in [MAJOR_VERSION, MINOR_VERSION, REVISION]
])

DEPENDENCIES = [
    'flake8',
    'praw',
    'progressbar'
]

setup(
    name='reddit_voting_script',
    version=PACKAGE_VERSION,
    description=DESCRIPTION,
    long_description=README,
    keywords='reddit',
    author='AJ McCrory',
    author_email='ajmccrory10@outlook.com',
    license='',
    packages=['reddit_voter'],
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    voter = reddit-voting.reddit-voting:main
    """,
)
