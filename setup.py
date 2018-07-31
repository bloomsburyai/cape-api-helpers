from package_settings import NAME, VERSION, PACKAGES, DESCRIPTION
from setuptools import setup

setup(
    name=NAME,
    version=VERSION,
    long_description=DESCRIPTION,
    author='Bloomsbury AI',
    author_email='contact@bloomsbury.ai',
    packages=PACKAGES,
    package_dir={'docqa': 'document-qa/docqa'},
    include_package_data=True,
    install_requires=[
        'pytest==3.6.4',
        'pydevd==1.1.1',
    ],
    package_data={
        '': ['*.*'],
    },
)
