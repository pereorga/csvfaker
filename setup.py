# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name='csvfaker',
    packages=['csvfaker'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': ['csvfaker = csvfaker.csvfaker:main']
    },
    install_requires=[
        'fake-factory',
    ],
    license='Apache License 2.0',
    url='https://github.com/pereorga/csvfaker',
    version='1.0.2',
    description='Generate a CSV file with fake data.',
    long_description=open('README.rst').read(),
    author='Pere Orga',
    author_email='pere@orga.cat',
)
