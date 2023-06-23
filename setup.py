from setuptools import setup, find_packages

setup(
    name='fnparser',
    version='1.0.0',
    author='Takano, Takeshi',
    author_email='takano.tak@gmail.com',
    description='for parsing file name',
    packages=['fnparser'],
    package_dir={'fnparser': 'src'},
    install_requires=["pandas", "numpy", "pathlib",]
)