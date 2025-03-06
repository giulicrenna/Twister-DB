from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="twisterdb",
    version="0.1.0",
    author="Giuliano Crenna",
    author_email="giulicrenna@gmail.com",
    description="A lightweight, local-based database solution for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giulicrenna/Twister-DB",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "colorama",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8",
            "black",
        ]
    },
    entry_points={
        "console_scripts": [
            "twisterdb=twisterdb.main:main",
        ],
    },
)
