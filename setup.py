from setuptools import setup, find_packages

setup (
    name = 'datavalidationtoolkit',
    version = '0.1.0',
    author = 'Mutuma Kimathi',
    author_email = 'Pius.mutuma.kimathi@gmail.com',
    description = 'A simple data validation toolkit',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Ppius6/Data-Validation-Toolkit',
    packages = find_packages(),
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)