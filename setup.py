import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='otus',
    version='0.1',
    packages=['otus'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='print links in console or save links in file',
    long_description=README,
    url='https://github.com/guillotine666/SetupPractice',
    author='guillotine666',
    author_email='xaxalox2@gmail.com',
    keywords=['search', 'savelink'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'find = otus.main:main',
        ]
    },
)
