"""
new_lambdata - a collection of Data Science helper functions
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open ("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="new-lambdata-ssbyrne89",
    version="0.0.2",
    author="ssbyrne89",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ssbyrne89/new_lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
