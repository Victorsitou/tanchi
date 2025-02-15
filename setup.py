from setuptools import setup

setup(
    name="hikari-tanchi",
    version="1.0.1",
    description="A signature parser for hikari's command handler tanjun.",
    url="https://github.com/thesadru/tanchi.py",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.9.0",
    author="thesadru",
    author_email="thesadru@gmail.com",
    keywords=["hikari"],
    install_requires=["hikari-tanjun"],
    packages=["tanchi"],
    include_package_data=True,
    package_data={"tanchi": ["py.typed"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications :: Chat",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
