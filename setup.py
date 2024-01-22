from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sizecalculator',
    version='0.1',
    author="Lpcodes",
    description="A Python package for displaying file size",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LpCodes/sizecalculator",
    project_urls={
        "Bug Tracker": "https://github.com/LpCodes/sizecalculator/issues",
        "Source Code": "https://github.com/LpCodes/sizecalculator",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    keywords='file size calculator utility command-line filesize python',
    entry_points={
        'console_scripts': [
            'sizecalculator = sizecalculator.sizecalculator:main',
        ],
    },
    python_requires=">=3.6",
    install_requires=[

    ],
)
