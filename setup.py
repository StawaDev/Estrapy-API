from setuptools import setup, find_packages

f = open("README.md", "r")
README = f.read()

setup(
    name="Estrapy-API",
    version="0.1.7",
    packages=find_packages(),
    install_requires=["requests"],
    license="MIT",
    url="https://github.com/StawaDev/Estrapy-API",
    author="StawaDev",
    description="A Basic Anime Image API Created By Stawa",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=[
        "python api",
        "anime",
        "anime gif",
        "roleplay gif",
        "wrapper anime gif",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
)
