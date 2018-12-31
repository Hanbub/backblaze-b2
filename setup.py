from setuptools import setup, find_packages

setup(
    name='backblazeb2',
    version='0.3.0',
    packages=find_packages(),
    license=open("LICENSE").read(),
    long_description=open('README.md').read(),
    install_requires=["pycrypto==2.6.1"]
)
