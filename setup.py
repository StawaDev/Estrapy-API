from setuptools import setup, find_packages

f = open("README.md", "r", encoding="utf-8")
README = f.read()

setup(
    name="Estrapy",
    version="0.2.7",
    packages=find_packages(),
    install_requires=["requests", "pygments"],
    extras_require={
        "cli": ["asyncclick", "tabulate", "anyio"],
    },
    license="MIT",
    url="https://github.com/StawaDev/Estrapy-API",
    project_urls={
        "Documentation": "https://stawa.gitbook.io/estraapi-documentation/",
        "Source": "https://github.com/StawaDev/Estrapy-API",
        "Tracker": "https://github.com/StawaDev/Estrapy-API/issues",
    },
    author="StawaDev",
    description="A Basic Wrapper Anime Image API with Many Features",
    long_description=README,
    long_description_content_type="text/markdown",
    entry_points="""
    [console_scripts]
    estrapy=Estrapy.cli:main
    estrapy help=Estrapy.cli:help
    estrapy save=Estrapy.cli:save
    """,
    keywords=[
        "python api",
        "anime",
        "anime gif",
        "roleplay gif",
        "wrapper anime gif",
        "osu",
        "osu api",
        "trivia",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Environment :: Console",
    ],
)
