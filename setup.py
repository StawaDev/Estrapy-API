from setuptools import setup, find_packages

f = open("README.md", "r")
README = f.read()

setup(
    name="Estrapy-API",
    version="0.2.1",
    packages=find_packages(),
    install_requires=["requests"],
    license="MIT",
    url="https://github.com/StawaDev/Estrapy-API",
    project_urls={
        "Documentation": "https://stawa.gitbook.io/estraapi-documentation/",
        "Source": "https://github.com/StawaDev/Estrapy-API",
        "Tracker": "https://github.com/StawaDev/Estrapy-API/issues",
    },
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
        "osu",
        "osu api",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
)
