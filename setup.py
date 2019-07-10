from setuptools import setup,find_packages
setup(
    name='fppy',
    version='1.0',
    description = 'fp functions for python',
    author = 'willngiht',
    author_email="willnight@yeah.net",
    url = 'https://github.com/jiangnight/fppy',
    packages=find_packages(exclude=["*.test", "*.test.*"])
)

