from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="pair-sniffer",
    version="0.1.",
    author="Alexandre Brilhante",
    author_email="alexandre.brilhante@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexandrebrilhante/pair-sniffer",
    project_urls={
        "Bug Tracker": "https://github.com/alexandrebrilhante/pair-sniffer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
