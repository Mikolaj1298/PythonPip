from setuptools import setup, find_packages

setup(
    name='azon-library',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='AZON Package',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/radosz99/azon-api-library',
    author='Mikołaj Kamiński',
    author_email='241388@student.pwr.edu.pl'
)
