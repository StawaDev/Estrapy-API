from setuptools import setup, find_packages

a = open("README.md", "r")
READMEFILE = a.read()

setup(
    name="Estrapy-API",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["requests"],
    license="MIT",
    url="https://github.com/StawaDev/Estrapy-API",
    description="A Basic Anime Image API Created By Stawa",
    long_description=READMEFILE,
    long_description_content_type="text/markdown",
    keywords=[
        "python api",
        "anime",
        "anime gif",
        "roleplay gif"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
