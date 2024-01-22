from setuptools import setup

setup(
    name='sizecalculator',
    version='0.1',
    packages=['sizecalculator'],
    entry_points={
        'console_scripts': [
            'sizecalculator = sizecalculator.sizecalculator:main',
        ],
    },
    install_requires=[
        # Any dependencies your package may have
    ],
)
