
import sys
try:
    # Setuptools entry point is slow.
    # If we have `festentrypoint` then use a fast entry point
    import fastentrypoints
except ImportError:
    sys.stdout.write('Not using fastentrypoints\n')
    pass


import setuptools
import os

HERE = os.path.dirname(__file__)

setuptools.setup(
    name='clixmod',
    version="0.1.0",
    author='Tal Wrii',
    author_email='talwrii@gmail.com',
    description='',
    license='GPLv3',
    keywords='',
    url='',
    packages=['clixmod'],
    long_description='See https://github.com/talwrii/clixmod',
    entry_points={
        'console_scripts': ['clixmod=clixmod.clixmod:main']
    },
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
    ],
    test_suite='nose.collector',
    install_requires=['lxml']
)
